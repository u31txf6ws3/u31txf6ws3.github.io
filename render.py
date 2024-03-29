from contextlib import redirect_stdout
from textwrap import dedent
import py2html
import io
import re


def replace_many(s, olds, news):
    for old, new in zip(olds, news):
        s = s.replace(old, new, 1)
    return s


def check_output(code, data):
    buf = io.StringIO()
    with redirect_stdout(buf):
        exec(dedent(code), {}, {**data, "render_template": render_template})
    return buf.getvalue()


def render_template(path, data=None):
    data = data or {}
    with open(path) as fin:
        if path.endswith(".py"):
            template, data = py2html.render_file(path)
        else:
            template = fin.read()

    code_blocks = re.findall(r"{{.+?}}", template, re.S)
    rendered = (
        check_output(block.lstrip("{").rstrip("}"), data) for block in code_blocks
    )
    return replace_many(template, code_blocks, rendered)
