from django.db import models

EXPANSION_TYPE = [
    ("E", "Expansion"),
    ("G", "Game"),
    ("S", "Stuff"),
    ("K", "Kit"),
    ("B", "Base"),
]

TRAIT_TYPE = [
    ("AM", "Ambition"),
    ("SK", "Skill"),
    ("LT", "Lot Trait"),
    ("LC", "Lot Challenge"),
    ("ST", "Sim Trait"),
]

# Create your models here.
class SimsPack(models.Model):
    name = models.CharField(max_length=40)
    icon = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices=EXPANSION_TYPE)

    def __str__(self): 
        return f'{self.name} the {self.type}'

class Trait(models.Model):
    name = models.CharField(max_length=40)
    icon = models.CharField(max_length=200)
    description = models.CharField()
    type = models.CharField(max_length=2, choices=TRAIT_TYPE)
    ambition_type = models.CharField(null=True, blank=True)
    trait_subtype = models.CharField(null=True, blank=True)
    effect = models.CharField(null=True, blank=True)
    pack = models.ForeignKey(SimsPack, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} is type {self.type} from {self.pack.name}'
