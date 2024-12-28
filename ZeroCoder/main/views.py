from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Первая страница</h1>")


def data(request):
    return HttpResponse("<h1>Страница data</h1>")

def test(request):
    return HttpResponse("<h1>Страница test</h1>")