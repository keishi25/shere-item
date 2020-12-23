from django.urls import path
from share.views import Share
from . import views

urlpatterns = [
    path(r'', Share.as_view(template_name='share/share.html'), name='share'),
]