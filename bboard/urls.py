from django.urls import path

from bboard.views import (index, by_rubric, BbCreateView,  # save, add
                          detail, BbDetailView, BbAddView, BbByRubricView, BbEditView, BbDeleteView)

app_name = 'bboard'

urlpatterns = [
    # path('add/', index, name='index'),
#     path('add/'<int:rubric_id>/$', by_rubric, name='by_rubric'),
    # path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),
    # path('add/save/', save, name='add_save'),
    # path('add/', BbAddView.as_view(), name='add'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('update/<init:pk>/', BbEditView.as_view(), name='update'),
    path('delete/<init:pk>/', BbDeleteView.as_view(), name='delete'),
    # path('add/', add, name='add'),
    # path('detail/<int:bb_id>/', detail, name='detail'),
    path('detail/<init:pk>/', BbDetailView.as_view(), name='detail'),
    path('', index, name='index'),
]



# re_path(r'^add/$', BbCreateView.as_view(), name='add'),
# re_path(r'^<int:rubric_id>/$', by_rubric, name='by_rubric'),
# re_path(r'^$', index, name='index')

