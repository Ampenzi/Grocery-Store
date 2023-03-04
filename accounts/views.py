from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import Signup, Login


class signup(View):
    def post(self, request):
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('login')
        return render(request, 'register.html', {'form':form})
    def get(self, request):
        form=Signup()
        return render(request, 'register.html', {'form':form})


class Login(LoginView):
    form_class = Login
    def form_valid(self, form):
        self.request.session.set_expiry(0)
        self.request.session.modified = True
        return super(Login, self).form_valid(form)


def home(request):
    return render(request, 'index.html')
