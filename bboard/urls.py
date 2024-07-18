from django.urls import path

from bboard.views import index, by_rubric, BbCreateView, save, add

app_name = 'bboard'

urlpatterns = [
#     path(r'^add/$', BbCreateView.as_view(), name='add'),
    path('add/save/', save, name='add_save'),
#     path(r'^<int:rubric_id>/$', by_rubric, name='by_rubric'),
    path('add/', add, name='add'),
#     path(r'^$', index, name='index'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
]



# re_path(r'^add/$', BbCreateView.as_view(), name='add'),
# re_path(r'^<int:rubric_id>/$', by_rubric, name='by_rubric'),
# re_path(r'^$', index, name='index')

