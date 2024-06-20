from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from bboard.forms import BbForm
from bboard.models import Bb, Rubrick


# def index(request):
#     s = 'Список объявлений\r\n\r\n\r\n'
#
#     for bb in Bb.objects.order_by('published'):
#         template = loader.get_template('bboard/index/html')
#         bbs = Bb.objects.order_by('published')
#         context = {'bbs': bbs}
#
#     return HttpResponse(template.render(context, request))


def index(request):
    bbs = Bb.objects.order_by('published')
    rubricks = Rubrick.objects.all()
    context = {'bbs': bbs, 'rubricks': rubricks}

    return render(request, 'bboard/index.html', context)

def by_rubrick(request, rubrick_id):
    bbs = Bb.objects.filter(rubrick=rubrick_id)
    rubricks = Rubrick.objects.all()
    current_rubrick = Rubrick.objects.get(pk=rubrick_id)
    context = {'bbs': bbs, 'rubricks': rubricks, 'current_rubrick': current_rubrick}

    return render(request, 'bboard/by_rubrick.html', context)


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('bboard:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubricks'] = Rubrick.objects.all()
        return context
