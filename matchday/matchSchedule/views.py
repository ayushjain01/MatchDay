from django.shortcuts import render
import random
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
from .models import Game, Team
def index(request):
    obj = Game.objects.all()
    print(str(obj))
   

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html",{'data' : obj})
def new(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    Game.objects.all().delete()

    num = Team.objects.values_list('name', flat=True).distinct()
    num = [""] + list(num)

    def teamer():
        start_team1 = random.randint(1, 8)
        start_team2 = random.randint(1, 8)
        while start_team1 == start_team2:
            start_team1 = random.randint(1, 8)
            start_team2 = random.randint(1, 8)
        return (start_team1, start_team2)

    def tempmaker(a):
        temp.append(a)
        for i in range(1, 9):
            if i == a:
                pass
            else:
                temp.append(i)

    def listshift(a):
        x1 = a.pop(4)
        x2 = a.pop(3)
        a.insert(1, x1)
        a.insert(7, x2)
        return a

    def swap(a):
        team1 = ""
        team2 = ""
        x = a.index(" ")
        team1 = a[:x]
        a = a[x+1:]
        x = a.index(" ")
        team2 = a[x+1:]
        return f"{team2} vs {team1}"

    def matchprint(a, n):
        for i in range(4):
            for j in range(4):
                if i == j:
                    game = f'{n[a[0][i]]} vs {n[a[1][j]]}'
                    if game not in played_list:
                        played_list.append(game)
                        game1 = Game(team1=n[a[0][i]], team2 = n[a[1][j]]) # create new model instance
                        game1.save()
                    else:
                        played_list.remove(game)
                        game1 = Game(team1=n[a[1][j]], team2 = n[a[0][i]]) # create new model instance
                        game1.save()
                else:
                    continue
    total_teams = 8
    rounds = 2
    teamlist = []
    team1 = []
    team2 = []
    temp = []
    played_list = []
    start_team1, start_team2 = teamer()
    tempmaker(start_team1)
    for ro in range(rounds):
        for i in range(total_teams-1):
            c = 0
            team1 = []
            team2 = []
            teamlist = []
            for j in temp:
                if c < 4:
                    team1.append(j)
                    c = c + 1
                else:
                    team2.append(j)
                    c = c + 1
            teamlist = [team1, team2]
            matchprint(teamlist, num)
            temp = listshift(temp)
        temp = []
        tempmaker(start_team2)
    
    response = redirect('/')
    return response


    