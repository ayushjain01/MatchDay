from django.db import models

# Create your models here.
class Team(models.Model):
    """Model representing a Team."""
    name = models.CharField(max_length=50, help_text='Enter the team name (e.g. Royal Challengers Bangalore)', primary_key = True)
    captain = models.CharField(max_length=100, help_text='Enter the team captain name (e.g. Virat Kohli)')
    owner = models.CharField(max_length=100, help_text='Enter the team owner name (e.g. Vijay Mallya)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    def getTeamName(self):
        return self.name
    def getCapName(self):
        return self.captain
    def getOwnName(self):
        return self.owner

class Player(models.Model):
    """Model representing a Player."""
    pid = models.IntegerField(primary_key = True, help_text='Enter Unique Player ID')
    name = models.CharField(max_length=50, help_text='Enter the player name (e.g. Virat Kohli)')
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True)
    role = models.CharField(max_length=100, help_text='Enter the player role (e.g. Batsman)')

    def __str__(self):
        """String for representing the Model object."""
        return str(self.pid) + ". " + self.name + " (" + str(self.team) + ")" 
    def getTeamName(self):
        return self.team
    def getName(self):
        return self.name
    def getRole(self):
        return self.role
class Game(models.Model):
    """Model representing a Game."""
    team1 = models.CharField(max_length=100,help_text='Enter the team name (e.g. Royal Challengers Bangalore)')
    team2 = models.CharField(max_length=100,help_text='Enter the team name (e.g. Royal Challengers Bangalore)')
    venue = models.CharField(max_length=100, help_text='Enter the game venue (e.g. Bangalore)')

    def __str__(self):
        """String for representing the Model object."""
        return self.team1 + ' vs ' + self.team2
    def getVenue(self):
        return self.venue
