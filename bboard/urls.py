from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, LogoutView
from django.urls import path, re_path

from bboard.models import Bb
from bboard.views import (index, by_rubric, BbCreateView, add_and_save, detail,
                          BbByRubricView, BbDetailView, BbAddView, BbEditView,
                          BbDeleteView, BbIndexView, BbRedirectView, edit,
                          rubrics)  # add, add_save

app_name = 'bboard'

urlpatterns = [
    path('rubrics/', rubrics, name='rubrics'),

    path('add/', BbCreateView.as_view(), name='add'),

    # path('update/<int:pk>/', BbEditView.as_view(), name='update'),
    path('update/<int:pk>/', edit, name='update'),

    path('delete/<int:pk>/', BbDeleteView.as_view(), name='delete'),
    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),

    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    # path('detail/<int:year>/<int:month>/<int:day>/<int:pk>/',
    #      BbDetailView.as_view(), name='detail'),
    path('detail/<int:year>/<int:month>/<int:day>/<int:pk>/',
         BbRedirectView.as_view(), name='old_detail'),

    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),

    path('accounts/password_change/',
         PasswordChangeView.as_view(template_name='registration/change_password.html'),
    name='password_change'),

    path('accounts/password_change/done/',
         PasswordChangeDoneView.as_view(template_name='registration/changed_password.html'),
    name='password_change_done'),

    path('', index, name='index'),
    # path('', BbIndexView.as_view(), name='index'),
]
