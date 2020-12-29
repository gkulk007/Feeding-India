from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import Subm
from .models import Submitform


def frontpage(request):
	if request.method=="POST":
		name = request.POST.get('name', '')
		phone = request.POST.get('phone', '')
		email = request.POST.get('email', '')
		line = request.POST.get('line', '')
		contact = Submitform(name=name,phone=phone, email=email, line=line)
		contact.save()

	return render(request, 'index.html')