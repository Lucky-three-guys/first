from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^postlist/',views.post_list,name="postlist")
]