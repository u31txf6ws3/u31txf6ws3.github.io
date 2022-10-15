#!/usr/bin/env python3
import json
import sys
from dataclasses import dataclass
from typing import Any, Callable, Iterable, Tuple, Iterator, TypeVar, List, Dict, Union, TextIO, Optional
from contextlib import redirect_stdout
import io
import itertools as itt
import html

T = TypeVar("T")


def take_until(pred: Callable[[T], bool], it: Iterable[T]) -> Tuple[List[T], Iterator[T]]:
    it = iter(it)
    out: List[T] = []
    empty = True
    for x in it:
        empty = False
        if pred(x):
            return out, itt.chain([x], it)
        out.append(x)
    if empty:
        raise StopIteration()
    return out, it


@dataclass(frozen=True)
class Comment:
    text: str

    @classmethod
    def from_lines(cls, lines: Iterable[str]) -> "Comment":
        return cls(
            "".join(s.replace("# ", "", 1) for s in lines).strip()
        )

    def render(self) -> str:
        if not self.text:
            return ""
        return f"<p>\n{self.text}\n</p>"


@dataclass(frozen=True)
class Code:
    code: str
    executable: bool = True

    @classmethod
    def from_lines(cls, lines: Iterable[str]) -> "Code":
        lines = iter(lines)
        head = next((l for l in lines if l.strip()), None)
        if not head:
            return cls("")
        if head.startswith("#$"):
            executable = False
        else:
            lines = itt.chain([head], lines)
            executable = True
        return cls("".join(lines).strip(), executable)

    def exec(self, globals_: Optional[Dict[str, Any]] = None) -> str:
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            try:
                exec(self.code, globals_ or globals())
            except:
                print(self.code, file=sys.stderr)
                raise
        return stdout.getvalue().strip()

    def render(self) -> str:
        if not self.code:
            return ""
        code = html.escape(self.code)
        output = html.escape(self.exec() if self.executable else "")
        if not output:
            return f"<pre>{self.code}</pre>"
        return f"<pre>{self.code}</pre>\n<pre># stdout\n{output}\n</pre>"


@dataclass(frozen=True)
class Post:
    metadata: Dict[str, str]
    sections: List[Union["Comment", "Code"]]

    @classmethod
    def from_file(cls, lines: Iterable[str]) -> "Post":
        metadata_block, lines = take_until(lambda l: not l.startswith("# "), lines)
        metadata = json.loads(Comment.from_lines(metadata_block).text)

        sections: List[Union["Comment", "Code"]] = []
        while True:
            try:
                comment_block, lines = take_until(lambda l: not l.startswith("# "), lines)
            except StopIteration:
                break
            comment = Comment.from_lines(comment_block)
            if comment.text:
                sections.append(comment)

            try:
                code_block, lines = take_until(lambda l: l.startswith("# "), lines)
            except StopIteration:
                break
            code = Code.from_lines(code_block)
            if code.code:
                sections.append(code)

        return cls(metadata, sections)

    def render(self) -> str:
        return "\n".join(s.render() for s in self.sections)


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(Post.from_file(f).render())
