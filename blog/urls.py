from django.urls import path
from .views import home, about, contact, services, pastprojects, demolitionform, newconform, renovateform, futureprojects
from .views import CreateReviewView, ListReviews, PostDetail


urlpatterns = [
    path('',home,name='home'),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
    path('services',services,name='services'),
    path('reviews',ListReviews.as_view(), name='reviews'),
    path('create',CreateReviewView.as_view(), name='create'),
    path('detail/<int:pk>', PostDetail.as_view(), name='detail'),
    path('pastprojects', pastprojects, name='pastprojects'),
    path('demolitionform', demolitionform, name='demolitionform'),
    path('newconform', newconform, name='newconform'),
    path('renovateform', renovateform, name='renovateform'),
    path('futureprojects', futureprojects, name='futureprojects'),

]