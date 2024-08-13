from aiohttp.web_fileresponse import FileResponse
from django.db.models import Count
from django.http import HttpResponse, Http404, StreamingHttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.template import loader
from django.urls import reverse_lazy, reverse
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView, DetailView, ArchiveIndexView, DateDetailView, RedirectView
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView

from bboard.forms import BbForm
from bboard.models import Bb, Rubric


# def index(request):#
#     template = loader.get_template('bboard/index.html')#
#     bbs = Bb.objects.order_by('-published')#
#     context = {'bbs': bbs}#
#
#     return HttpResponse(template.render(context, request))#


def index(request):
    bbs = Bb.objects.order_by('-published')
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}

    return render(request, 'bboard/index.html', context)

#def index(request):#
#    resp = HttpResponse("Здесь будет", content_type='text/plain; charset=utf-8')#
#    resp.write("Главная")#
#    resp.writelines(('страница','сайта'))#

# def index(request): #
#     resp_content = ("Здесь будет", " главная", " страница", " сайта") #
#     resp = StreamingHttpResponse(resp_content, content_type='text/plain; charset=utf-8') #
#     return  resp #

# def file_resp(request):
#     filename = r'C:/images/image.png'
#     return FileResponse(open(filename, 'rb'))

# def json_resp(request):
#     data = {'title': 'Мотоцикл', 'content': 'пердящий', 'price': 10000.0}
#     return render(request, 'bboard/index.html', context)



def by_rubric(request, rubric_id):
    # bbs = Bb.objects.filter(rubric=rubric_id)
    # rubrics = Rubric.objects.annotate(cnt=Count('bb').filter(cnt__gt=0))
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)

    # bbs = current_rubric.entries.all()
    # bbs = current_rubric.bb_set.all()
    bbs = get_list_or_404(Bb, rubric=rubric_id)

    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}

    return render(request, 'bboard/by_rubric.html', context)

class BbByRubricView(TemplateView):
    template_name = 'bboard/by_rubric.html'
    context_object_name = 'bbs'

    def get_queryset(self):
        return Bb.objects.fiter(rubric=self.kwargs['rubric_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.annotate(cnt=Count('bb').filter(cnt__gt=0))
        context['current_rubric'] = Rubric.objects.get(pk=self.kwargs['rubric_id'])
        return context

class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    # success_url = reverse_lazy('bboard:index')
    success_url = ('/{rubric_id}')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.annotate(cnt=Count('bb').filter(cnt__gt=0))
        return context


class BbEditView(UpdateView):
    model = Bb
    form_class = BbForm
    success_url = '/{rubric}'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.annotate(cnt=Count('bb').filter(cnt__gt=0))
        return context


class BbAddView(FormView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    initial = {'price': 0.0}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.annotate(cnt=Count('bb').filter(cnt__gt=0))
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object

    def get_succes_url(self):
        return reverse('bboard:by_rubric',
                       kwargs={'rubric_id': self.object.cleaned_data['rubric'].pk})


# def add(request):
#     bbf = BbForm()
#     context = {'form':bbf}
#     return render(request, 'bboard/create.html', context)

#
# class HttpResponseRedirect:
#     pass


# def save(request):
#     bbf = BbForm(request.POST)
#
#     if bbf.is_valid():
#         bbf.save()
#         return HttpResponseRedirect(reverse('bboard:by_rubric',
#             kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}))
#     else:
#         context = {'form': bbf}
#         return render(request, 'bboard/create.html', context)

@require_http_methods(['GET', 'POST'])
def add_and_save(request):
    if request.method == 'POST':
        bbf = BbForm(request.POST)

        if bbf.is_valid():
            bbf.save()
            # return HttpResponseRedirect(reverse('bboard:by_rubric',
            #                                     kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}))
            return redirect('bboard:by_rubric',
                            rubric_id=bbf.cleaned_data['rubric'].pk)
        else:
            context = {'form': bbf}
            return render(request, 'bboard/create.html', context)

    else:
        bbf = BbForm()
        context = {'form': bbf}
        return render(request, 'bboard/create.html', context)

def detail(request, bb_id):
    bb = get_object_or_404(Bb, pk=bb_id)

    rubrics = Rubric.objects.annotate(cnt=Count('bb')).filter(cnt__gt=0)
    context = {'bb': bb, 'rubrics': rubrics}

    return render(request, 'bboard/detail.html', context)


class BbDetailView(DetailView):
    model = Bb

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.annotate(cnt=Count('bb')).filter(cnt__gt=0)
        return context


class BbDeleteView(DeleteView):
    model = Bb
    success_url = reverse_lazy('bboard:index')

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

class BbIndexView(ArchiveIndexView):
    model = Bb
    data_field = 'published'
    date_list_period = 'year'
    template_name = 'bboard/index.html'
    context_object_name = 'bbs'
    allow_empty = True
    # allow_future = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.annotate(cnt=Count('bb').filter(cnt__gt=0))
        return context

class BbDetailView(DateDetailView):
    model = Bb
    date_field = 'published'
    month_format = '%m'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.annotate(cnt=Count('bb').filter(cnt__gt=0))
        return context

class BbRedirectView(RedirectView):
    url = 'detail'