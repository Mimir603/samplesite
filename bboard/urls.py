from django.urls import path

from bboard.views import index, by_rubrick


app_name = 'bboard'

urlpatterns = [
    path('<int:rubrick_id>/', by_rubrick, name='by_rubrick'),
    path('', index, name='index')
]
