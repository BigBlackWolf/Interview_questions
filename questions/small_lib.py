from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter


def code_to_html(text):
    return highlight(text, PythonLexer(), HtmlFormatter())
