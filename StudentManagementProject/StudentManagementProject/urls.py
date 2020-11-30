from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from studentapp import views
app_name = "studentapp"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('application/', views.application, name = 'application'),
    path('registration/', views.registration, name = 'registration'),
    path('condidates/', views.condidates, name= 'condidates'),
    path('DepartmentWise/', views.DepartmentWise, name = 'DepartmentWise'),
    path('department/details', views.details, name='details'),
    path('SelectStudentList', views.SelectStudentList, name='SelectStudentList'),



]
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
