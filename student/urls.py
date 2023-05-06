from django.urls import path, include
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, 
    PasswordResetCompleteView, LoginView, LogoutView
    )
from .views import (
        profile, profile_single, admin_panel, 
        profile_update, change_password, 
        LecturerListView, StudentListView, 
        staff_add_view, edit_staff, 
        delete_staff, student_add_view, 
        edit_student, delete_student, validate_username, register
    )
from .forms import EmailValidationOnForgotPassword


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    
    path('profile/', profile, name='profile'),
    path('profile/<int:id>/detail/', profile_single, name='profile_single'),
    path('setting/', profile_update, name='edit_profile'),
    path('change_password/', change_password, name='change_password'),

    path('profs/', LecturerListView.as_view(), name='prof_list'),
    path('prof/add/', staff_add_view, name='add_prof'),
    path('prof/<int:pk>/edit/', edit_staff, name='prof_edit'),
    path('prof/<int:pk>/delete/', delete_staff, name='prof_delete'),

    path('students/', StudentListView.as_view(), name='student_list'),
    path('student/add/', student_add_view, name='add_student'),
    path('student/<int:pk>/edit/', edit_student, name='student_edit'),
    path('students/<int:pk>/delete/', delete_student, name='student_delete'),

    path('ajax/validate-username/', validate_username, name='validate_username'),

    
    path('admin_panel/', admin_panel, name='admin_panel'),

]
