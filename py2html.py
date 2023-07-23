import html
import io
import json
import sys
from contextlib import redirect_stdout
from dataclasses import dataclass


class NotValid(Exception):
    pass


@dataclass(frozen=True)
class Comment:
    content: str

    def __add__(self, other):
        if isinstance(other, Comment):
            return Comment(self.content + other.content)
        raise NotValid()

    def render(self):
        if not self.content:
            return ""
        return f"<p>\n{self.content}\n</p>"


@dataclass(frozen=True)
class Code:
    content: str

    def __add__(self, other):
        if isinstance(other, Code):
            return Code(self.content + other.content)
        if isinstance(other, Newline):
            return Code(self.content + "\n")
        raise NotValid()

    def exec(self, globals_):
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            try:
                exec(self.content, globals_)
            except:
                print(self.content, file=sys.stderr)
                raise
        return Stdout(stdout.getvalue().strip())

    def render(self):
        if not self.content:
            return ""
        return f"<pre>{html.escape(self.content).rstrip()}</pre>"


@dataclass(frozen=True)
class Stdout:
    content: str

    def __add__(self, other):
        raise NotValid()

    def render(self):
        if not self.content:
            return ""
        return f"<pre>#[stdout]\n{html.escape(self.content)}</pre>"


@dataclass(frozen=True)
class NoExecFlag:
    def __add__(self, other):
        if isinstance(other, Code):
            return NonExecutableCode(other.content)
        raise NotValid()

    def render(self):
        raise ValueError()


@dataclass(frozen=True)
class NonExecutableCode:
    content: str

    def __add__(self, other):
        if isinstance(other, Code):
            return NonExecutableCode(self.content + other.content)
        if isinstance(other, Newline):
            return NonExecutableCode(self.content + "\n")
        raise NotValid()

    def render(self):
        if not self.content:
            return ""
        return f"<pre>{html.escape(self.content)}</pre>"


@dataclass(frozen=True)
class Newline:
    def __add__(self, other):
        raise NotValid()

    def render(self):
        return ""


def parse_line(line):
    if not line.strip():
        return Newline()
    if line.startswith("# "):
        return Comment(line[2:])
    if line.startswith("#$"):
        return NoExecFlag()
    return Code(line)


def parse_line_stream(lines):
    elements = [parse_line(next(lines))]
    for line in lines:
        el = parse_line(line)
        try:
            elements[-1] = elements[-1] + el
        except NotValid:
            elements.append(el)
    return elements


def render_file(path):
    out = []
    with open(path) as f:
        els = parse_line_stream(f)
    metadata = els.pop(0)
    gl = {}
    for el in els:
        out.append(el.render())
        if isinstance(el, Code):
            out.append(el.exec(gl).render())
    return "\n".join(out), json.loads(metadata.content)
