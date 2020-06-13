from django.urls import path

from .views import (
    loginView, 
    registerView, 
    logoutView, 
    tambahIklan, 
    UpdateUser,
    UpdateIklan,
    ManageIklan,
    DeleteIklan,
    DetailIklan,
)
app_name = 'mitra'
urlpatterns = [
    path('login', loginView, name='login'),
    path('register', registerView, name='registrasi'),
    path('logout', logoutView, name='logout'),
    path('tambahIklan', tambahIklan, name='tambahIklan'),
    path('updateUser/<int:pk>', UpdateUser.as_view(), name='updateUser'),
    path('updateIklan/<int:pk>', UpdateIklan.as_view(), name='updateIklan'),
    path('iklanSaya', ManageIklan.as_view(), name='iklanSaya'),
    path('deleteIklan/<int:pk>', DeleteIklan.as_view(), name='deleteIklan'),
    path('detailIklan/<str:slug>', DetailIklan.as_view(), name='detailIklan'),
]