import html
import io
import json
import sys
from contextlib import redirect_stdout
from dataclasses import dataclass
from typing import Any, NoReturn, Iterator


class NotValid(Exception):
    pass


@dataclass(frozen=True)
class Comment:
    content: str

    def __add__(self, other: Any) -> "Comment":
        if isinstance(other, Comment):
            return Comment(self.content + other.content)
        raise NotValid()

    def render(self) -> str:
        if not self.content:
            return ""
        return f"<p>\n{self.content}\n</p>"


@dataclass(frozen=True)
class Code:
    content: str

    def __add__(self, other: Any) -> "Code":
        if isinstance(other, Code):
            return Code(self.content + other.content)
        if isinstance(other, Newline):
            return Code(self.content + "\n")
        raise NotValid()

    def exec(self, globals_: dict[str, Any]) -> "Stdout":
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            try:
                exec(self.content, globals_)
            except:
                print(self.content, file=sys.stderr)
                raise
        return Stdout(stdout.getvalue().strip())

    def render(self) -> str:
        if not self.content:
            return ""
        return f"<pre>{html.escape(self.content).rstrip()}</pre>"


@dataclass(frozen=True)
class Stdout:
    content: str

    def __add__(self, other: Any) -> "NoReturn":
        raise NotValid()

    def render(self) -> str:
        if not self.content:
            return ""
        return f"<pre>#[stdout]\n{html.escape(self.content)}</pre>"


@dataclass(frozen=True)
class NoExecFlag:
    def __add__(self, other: Any) -> "NonExecutableCode":
        if isinstance(other, Code):
            return NonExecutableCode(other.content)
        raise NotValid()

    def render(self) -> NoReturn:
        raise ValueError()


@dataclass(frozen=True)
class NonExecutableCode:
    content: str

    def __add__(self, other: Any) -> "NonExecutableCode":
        if isinstance(other, Code):
            return NonExecutableCode(self.content + other.content)
        if isinstance(other, Newline):
            return NonExecutableCode(self.content + "\n")
        raise NotValid()

    def render(self) -> str:
        if not self.content:
            return ""
        return f"<pre>{html.escape(self.content).rstrip()}</pre>"


@dataclass(frozen=True)
class Newline:
    def __add__(self, other: Any) -> NoReturn:
        raise NotValid()

    def render(self) -> str:
        return ""


Renderable = Newline | Comment | Code | NoExecFlag | NonExecutableCode


def parse_line(line: str) -> Renderable:
    if not line.strip():
        return Newline()
    if line.startswith("# "):
        return Comment(line[2:])
    if line.startswith("#$"):
        return NoExecFlag()
    return Code(line)


def parse_line_stream(lines: Iterator[str]) -> list[Renderable]:
    elements: list[Renderable] = [parse_line(next(lines))]
    for line in lines:
        el = parse_line(line)
        try:
            elements[-1] = elements[-1] + el
        except NotValid:
            elements.append(el)
    return elements


def render_file(path: str) -> tuple[str, dict[str, Any]]:
    out = []
    with open(path) as f:
        els = parse_line_stream(f)
    metadata = els.pop(0)
    assert isinstance(metadata, Comment), "File must start with a comment block"
    gl: dict[str, Any] = {}
    for el in els:
        out.append(el.render())
        if isinstance(el, Code):
            out.append(el.exec(gl).render())
    return "\n".join(out), json.loads(metadata.content)
