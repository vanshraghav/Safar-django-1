from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('',views.index),
    path('delhi',views.explore_delhi),
    path('plan',views.prims),
    path('chennai',views.explore_chennai),
    path('mumbai',views.explore_mumbai),
    path('surat',views.explore_surat),
    path('contactus',views.contact_us),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)