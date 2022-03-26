from django.http import request
from django.shortcuts import render,HttpResponse
from tution.models import Contact
from django.views.generic import TemplateView


def home(request):
    name=['ayman','rejoan','tulfa','nahida','nadira']
    context={
        'name':name
    }
    return render(request, 'home.html', context)
    
class HomeView(TemplateView):
    template_name='home.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['msg']="welcome to my website"
        context['msg2']="welcome to my website again"
        return context