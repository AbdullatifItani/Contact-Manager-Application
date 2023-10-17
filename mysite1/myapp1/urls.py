from django.urls import path
from . import views
from mysite1.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-contact'),
    path('update/<int:contact_id>', views.update_contact, name = 'update-contact'),
    path('delete/<int:contact_id>', views.delete_contact, name = 'delete-contact')
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)