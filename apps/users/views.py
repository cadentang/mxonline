from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.


class LoginView(View):
	def get(self, request):
		return render(request, 'login.html', {})
	def post(self, request):
		login_form = LoginForm(request.POST)
		user_name = request.POST.get("username", "")
		pass_word = request.POST.get("password", "")
		user = authenticate(username= user_name, password=pass_word)
		if user is not None:
			login(request, user)
			return render(request, "index.html")
		else:
			return render(request, "login.html", {"msg": "用户名或者密码错误！"})

