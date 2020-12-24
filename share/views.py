from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class Share(TemplateView):

    template_name = 'share/share.html'

    def get(self, request, *args, **kwargs):

        data_dict = {"a": 2}

        return render(request, 'share/share.html', data_dict)

