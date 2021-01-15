from django.http import HttpResponse, response
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello World")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def result(request, question_id):
    """
    docstring
    """
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're votting on question %s" % question_id)
