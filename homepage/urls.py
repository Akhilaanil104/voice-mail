from django.urls import path, include
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.login_view, name="login"),
    path('compose/', views.compose_view, name="compose"),
    path('inbox/', views.read_received_emails, name="inbox"),
    path('sent/', views.read_sent_emails, name="sent"),
    path('trash/', views.trash_view, name="trash"),
    path('options/', views.options_view, name="options"),
    # path('read/',views.read_emails ,name='read')
]
