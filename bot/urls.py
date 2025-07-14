
from django.views.generic.base import TemplateView
from django.urls import path
from .views import BotView

urlpatterns = [
    path('handle/', BotView.as_view(), name='bot_handle')
]