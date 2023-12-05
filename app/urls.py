from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='user_dashboard'),
    path('createForm/', views.create_form, name='creat_form'),
    path('getForm/<int:form_id>/', views.get_form, name='get_form'),
    path('collectResponse/<int:form_id>', views.collect_response, name='collect_response'),
]