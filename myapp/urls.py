from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('our_view/',views.our_view,name='our_view'),
    path('search/', views.search, name='search'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]
