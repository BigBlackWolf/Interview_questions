from django.urls import path
from .views import PythonQuestions

urlpatterns = [
    path('', PythonQuestions.as_view(), name='python')
]