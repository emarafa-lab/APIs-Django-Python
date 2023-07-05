from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render

class HelloWorld(View):
    def get(self, request):
        data = {
            'name': 'Emanuel Rafael',
            'years': 21,
            'codes': ['Python', 'Django', 'Java']
        }
        return render(request, 'hello_world.html', data)