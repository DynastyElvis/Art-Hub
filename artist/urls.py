from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('', views.home, name='index'),
    path('about', views.about, name='about'),
    path('postImage/', views.post_image, name='postImage'),
    path('photos', views.photos, name='photos'),
    path('profile/<username>', views.profile, name='profile'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


