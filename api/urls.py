from django.urls import path

from api import views


urlpatterns = [
    path('tokenize', views.tokenize_view),
    path('pos_tag', views.pos_tag_view),
    path('ner', views.ner_view),
]
