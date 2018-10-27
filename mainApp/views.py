from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from django import views
from mainApp.forms import VidOpenForm
from embed_video.backends import detect_backend
from django.contrib.auth import authenticate, login
from mainApp.models import *
# Create your views here.


class HomePageView(views.View):
	def get(self, request, *args, **kwargs):
		return render(request, 'home/index.html' , {})

home_page = HomePageView.as_view()

class VideoSearchView(views.View):
	def get(self, request, *args, **kwargs):
		form = VidOpenForm()
		return render(request, 'vidsearch/index.html' , {"form": form})

	def post(self, request, *args, **kwargs):
		print(request.POST)
		video = detect_backend(request.POST['url'])
		cc_url = "https://www.youtube.com/api/timedtext?lang=en&v=%s" %(video.get_code())
		vid_url = video.get_code()
		return render(request, 'vidsearch/view.html', {"my_video": video, "cc_url": cc_url, 'vid_url': vid_url})

vid_search_page = VideoSearchView.as_view()


class LoginView(views.View):
	def get(self, request, *args, **kwargs):
		return render(request, "home/login.html", {})

	def post(self, request, *args, **kwargs):
		user = authenticate(username = request.POST['username'], password = request.POST['pass'])
		if user is not None:
			login(request, user)
			return HttpResponseRedirect("/site/groups/")
		return render(request, "home/login.html", {"failed": True})

login_page = LoginView.as_view()

class GroupsView(views.View):
	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return HttpResponseRedirect("/site/login/")
		return render(request, "home/studyGroup.html", {"objects": StudyGroup.objects.all()})

	def post(self, request, *args, **kwargs):
		try:
			time = request.POST['time']
			venue = request.POST['venue']
			date = request.POST['date']
			topic = request.POST['topic']
			StudyGroup.objects.create(time=time, venue=venue, date=date, topic=topic, by=request.user)
			return HttpResponseRedirect("/site/groups")
		except:
			raise Http404
groups_page = GroupsView.as_view()