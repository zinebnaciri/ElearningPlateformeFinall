from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.views.generic import CreateView, ListView
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

from .decorators import lecturer_required, student_required, admin_required

from .forms import StaffAddForm, StudentAddForm, ProfileUpdateForm
from .models import User, Student


def validate_username(request):
    username = request.GET.get("username", None)
    data = {
        "is_taken": User.objects.filter(username__iexact = username).exists()
    }
    return JsonResponse (data)


def register(request):
    if request.method == 'POST':
        form = StudentAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account created successfuly.')
        else:
            messages.error(request, f'Somthing is not correct, please fill all fields correctly.')
    else:
        form = StudentAddForm(request.POST)
    return render(request, "registration/register.html", {'form': form})


@login_required
def profile(request):
    """ Show profile of any user that fire out the request """
    if request.user.is_student:
        level = Student.objects.get(student__pk=request.user.id)
        context = {
            'title': request.user.get_full_name,
            'level': level,
        }
        return render(request, 'student/profile.html', context)
    else:
        staff = User.objects.filter(is_lecturer=True)
        return render(request, 'student/profile.html', {
            'title': request.user.get_full_name,
        })


@login_required
@admin_required
def profile_single(request, id):
    """ Show profile of any selected user """
    if request.user.id == id:
        return redirect("/profile/")
    user = User.objects.get(pk=id)
    if user.is_student:
        student = Student.objects.get(student__pk=id)
        context = {
            'title': user.get_full_name,
            'user': user,
            "user_type": "student",
            'student': student,
        }
        return render(request, 'student/profile_single.html', context)
    else:
        context = {
            'title': user.get_full_name,
            "user": user,
            "user_type": "superuser",
        }
        return render(request, 'student/profile_single.html', context)


@login_required
@admin_required
def admin_panel(request):
    return render(request, 'admin_panel.html', {})
# ########################################################

@login_required
def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'student/profile_info_change.html', {
        'title': 'Elearning',
        'form': form,
    })


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error(s) below. ')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'student/password_change.html', {
        'form': form,
    })
# ########################################################

@login_required
@admin_required
def staff_add_view(request):
    if request.method == 'POST':
        form = StaffAddForm(request.POST)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if form.is_valid():
            form.save()
            messages.success(request, "prof " + first_name + ' ' + last_name + " has been created.")
            return redirect("prof_list")
    else:
        form = StaffAddForm()

    context = {
        'title': 'Elearning',
        'form': form,
    }

    return render(request, 'student/add_prof.html', context)


@login_required
@admin_required
def edit_staff(request, pk):
    instance = get_object_or_404(User, is_lecturer=True, pk=pk)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=instance)
        full_name = instance.get_full_name
        if form.is_valid():
            form.save()

            messages.success(request, 'prof ' + full_name + ' has been updated.')
            return redirect('prof_list')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProfileUpdateForm(instance=instance)
    return render(request, 'student/edit_prof.html', {
        'title': 'Elearning',
        'form': form,
    })


@method_decorator([login_required, admin_required], name='dispatch')
class LecturerListView(ListView):
    queryset = User.objects.filter(is_lecturer=True)
    template_name = "student/prof_list.html"
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Elearning"
        return context

@login_required
@admin_required
def delete_staff(request, pk):
    lecturer = get_object_or_404(User, pk=pk)
    full_name = lecturer.get_full_name
    lecturer.delete()
    messages.success(request, 'prof ' + full_name + ' has been deleted.')
    return redirect('prof_list')
# ########################################################

@login_required
@admin_required
def student_add_view(request):
    if request.method == 'POST':
        form = StudentAddForm(request.POST)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if form.is_valid():
            form.save()
            messages.success(request, 'Account for ' + first_name + ' ' + last_name + ' has been created.')
            return redirect('student_list')
        else:
            messages.error(request, 'Correct the error(s) below.')
    else:
        form = StudentAddForm()

    return render(request, 'student/add_student.html', {
        'title': "Elearning",
        'form': form
    })


@login_required
@admin_required
def edit_student(request, pk):
    # instance = User.objects.get(pk=pk)
    instance = get_object_or_404(User, is_student=True, pk=pk)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=instance)
        full_name = instance.get_full_name
        if form.is_valid():
            form.save()

            messages.success(request, ('Student ' + full_name + ' has been updated.'))
            return redirect('student_list')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProfileUpdateForm(instance=instance)
    return render(request, 'student/edit_student.html', {
        'title': 'Elearning',
        'form': form,
    })


@method_decorator([login_required, admin_required], name='dispatch')
class StudentListView(ListView):
    template_name = "student/student_list.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = Student.objects.all()
        query = self.request.GET.get('student_id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Elearning"
        return context


@login_required
@admin_required
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    messages.success(request, 'Student has been deleted.')
    return redirect('student_list')
