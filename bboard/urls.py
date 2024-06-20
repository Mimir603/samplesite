from django.urls import path

from bboard.views import index, by_rubrick, BbCreateView

app_name = 'bboard'

urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubrick_id>/', by_rubrick, name='by_rubrick'),
    path('', index, name='index')
]
