from django.urls import path
from programmes.views import *
app_name="programmes"
urlpatterns = [
    path('', NiveauListView.as_view(), name="niveaulist"),
    path('<slug:slug>', MatiereListView.as_view(), name="matierelist"),
    path('<str:niveau>/<slug:slug>/', LessonListView.as_view(), name="lessonlist"),
    path('<str:niveau>/<str:slug>/create/', LessonCreateView.as_view(), name="lessoncreate"),
    path('<str:niveau>/<str:matiere>/<slug:slug>/', LessonListViewDetail.as_view(), name="lessonlistdetail"),
    path('<str:niveau>/<str:matiere>/<slug:slug>/update/',LessonUpdateView.as_view(), name="lessonupdate"),
    path('<str:niveau>/<str:matiere>/<slug:slug>/delete', LessonDeleteView.as_view(), name="lessondelete"),
    
]