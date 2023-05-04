
from django.shortcuts import render
from .models import *
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView, FormView
from .form import LessonForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


class NiveauListView(ListView):
    context_object_name = 'niveaux'
    model = Niveaux
    template_name = 'programmes/niveaulist.html'

class MatiereListView(DetailView):
    context_object_name = 'niveau'
    model = Niveaux
    template_name = 'programmes/matierelist.html'

class LessonListView(DetailView):
    context_object_name = 'matieres'
    model = Matiere
    template_name = 'programmes/lessonlist.html'

class LessonListViewDetail(DetailView):
    context_object_name = 'lesson'
    model = Lesson
    template_name = 'programmes/lessonlistdetail.html'

class LessonCreateView(CreateView):
    form_class = LessonForm
    context_object_name = 'matieres'
    model = Matiere
    template_name = 'programmes/lessoncreate.html'

    def get_success_url(self):
        self.object = self.get_object()
        niveau = self.object.niveau
        return reverse_lazy('programmes:lessonlist', kwargs={'niveau':niveau, 'slug':self.object.slug})

    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        ls = form.save(commit=False)
        ls.creer_par = self.request.user
        ls.niveau = self.object.niveau
        ls.matiere = self.object
        ls.save()
        return HttpResponseRedirect(self.get_success_url())
    


class LessonUpdateView(UpdateView):
    fields = ('nom', 'position', 'pdf', 'fpe')
    context_object_name = 'lesson'
    model = Lesson
    template_name = 'programmes/lessonupdate.html'

class LessonDeleteView(DeleteView):
    model = Lesson
    context_object_name = "lesson"
    template_name = 'programmes/lessondelete.html'
    
    def get_success_url(self):
        niveau = self.object.niveau
        matiere = self.object.matiere
        return reverse_lazy("programmes:lessonlist", kwargs={'niveau':niveau, 'slug':matiere.slug})
      