from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import HelloWorld


# Create your views here.


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm  # == create.html 안의 {{ form }} 와 같음
    success_url = reverse_lazy('accountapp:hello_world')
    # 함수형, 클래스 형 방식의 차이점 에서 reverse, reverse_lazy 로 나뉜다.
    # 함수형 방식 : reverse / 클래스 형 방식 : reverse_lazy
    template_name = 'accountapp/create.html'
