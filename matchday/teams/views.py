from django.shortcuts import render
from matchSchedule import models
# Create your views here.
def home(request):
    obj = models.Player.objects.all()
    print(str(obj))
    return render(request, "base.html",{'data' : obj})