from django.conf.urls.static import static
from django.urls import path

from wick_shop import settings
from . import views


urlpatterns = [
    path('', views.WickView.as_view()),
    path("search/", views.Search.as_view(), name='search'),
    path('sign_in/', views.SingIN.as_view(), name='sign_in'),
    path('<slug:slug>/', views.WickInfo.as_view(), name='wick_detail'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)