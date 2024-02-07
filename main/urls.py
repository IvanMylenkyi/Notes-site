from django.contrib import admin
from django.urls import path
from . import views
# add redirects
urlpatterns = [
    path('home/',views.index,name='home'),
    path('about',views.about,name='about'),
    path('create',views.create,name='create'),
    path('task/<int:pk>', views.TaskDetailsView.as_view(),name='tasks'),
    path('task/<int:pk>/edit', views.TaskUpdateView.as_view(),name='edit'),
    path('task/<int:pk>/delete', views.TaskDeleteView.as_view(),name='delete'),

]