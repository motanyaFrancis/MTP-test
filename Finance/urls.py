from django.urls import path

from . import views

urlpatterns = [
    path('imprests/', views.imprests_view, name='imprests'),
    path('imprest/details/', views.imprest_detail_view, name='imprests-details'),
]