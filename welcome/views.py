from django.shortcuts import render
from django.views import generic
from django.contrib import messages

from . import forms
from .models import NewMember


class IndexView(generic.View):
    pass


class WelcomeView(generic.View):
    template_name = 'welcome/welcome.html'

    def get(self, request):
        form = forms.WelcomeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = forms.WelcomeForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            del cd['captcha']
            NewMember.objects.create(**cd)
            messages.add_message(request,
                                 messages.SUCCESS,
                                 '报名成功，请<a href="http://jq.qq.com/?_wv=1027&k=40A4Y38" target="_blank">点击此处加入2017KS招新群</a>',
                                 extra_tags='safe')
            return render(request, self.template_name, {'form': form})
        else:
            messages.add_message(request, messages.WARNING, '报名失败，请查看各项后的错误提示。')
            return render(request, self.template_name, {'form': form})
