from django.views import View
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter


class PythonQuestions(View):

    def get(self, request, *args, **kwargs):
        text = 'class Test:'
        result = {'text': highlight(text, PythonLexer(), HtmlFormatter())}
        return render(request, context=result, template_name='index.html')


class Terminal:
    pass
