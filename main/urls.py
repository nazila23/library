from django.urls import path

from . import views

urlpatterns = [
    path('', views.form_pinjam, name='form_pinjam'), 
    path('<id>/delete/', views.deleteindex),
    path('<id>/detail/', views.detailindex),
    path('<id>/update/', views.updateindex),
    path('sejarah/', views.sejarah, name='sejarah'), 
    path('visi/', views.visi, name='visi'), 
    path('<id>/buku_dipinjam/', views.buku_dipinjam), 
    path('index/', views.index, name='index'),
    path('dftr/', views.dftr, name='dftr'),
    path('<id>/edit_dftr/', views.edit_dftr),
    path('<id>/delete_dftr/', views.delete_dftr),
     path('<id>/detail_dftr/', views.detail_dftr),
    path('kembali/', views.kembali, name='kembali'),
    
]