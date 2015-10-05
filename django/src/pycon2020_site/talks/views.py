from django.http import HttpResponse
from django.shortcuts import render
from .models import Talk


# Create your views here.
def talk_list(request):
    talks = Talk.objects.all()
    output = ', '.join([str(talk) for talk in talks])
    return HttpResponse(output)


def talk_template_list(request):
    talks = Talk.objects.all()
    return render(request, 'talks/talk_list.html', {'talks': talks})
