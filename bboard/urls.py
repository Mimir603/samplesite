from django.urls import path

from bboard.views import (index, by_rubric, BbCreateView,  # save, add
                          detail, BbDetailView, BbAddView, BbByRubricView, BbEditView, BbDeleteView)

from django.views.generic.base import TemplateView, RedirectView

app_name = 'bboard'

urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('update/<int:pk>/', BbEditView.as_view(), name='update'),
    path('delete/<int:pk>/', BbDeleteView.as_view(), name='delete'),
    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),
    # path('detail/<init:pk>/', BbDetailView.as_view(), name='detail'),
    path('detail/<int:year>/<int:month>/<int:day>/<int:pk>/', BbDetailView.as_view(), name='detail'),
]



# re_path(r'^add/$', BbCreateView.as_view(), name='add'),
# re_path(r'^<int:rubric_id>/$', by_rubric, name='by_rubric'),
# re_path(r'^$', index, name='index')

