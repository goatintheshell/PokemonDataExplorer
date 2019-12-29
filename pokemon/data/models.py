from django.db import models

# Create your models here.
class Pokemon(models.Model):
    abilities = models.TextField(blank=True, null=True)
    attack = models.IntegerField(blank=True, null=True)
    base_egg_steps = models.IntegerField(blank=True, null=True)
    base_happiness = models.IntegerField(blank=True, null=True)
    base_total = models.IntegerField(blank=True, null=True)
    capture_rate = models.IntegerField(blank=True, null=True)
    classification = models.TextField(blank=True, null=True)
    defense = models.IntegerField(blank=True, null=True)
    experience_growth = models.IntegerField(blank=True, null=True)
    height_m = models.FloatField(blank=True, null=True)
    hp = models.IntegerField(blank=True, null=True)
    japanese_name = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    percentage_male = models.FloatField(blank=True, null=True)
    pokedex_number = models.IntegerField(blank=True, null=True)
    sp_attack = models.IntegerField(blank=True, null=True)
    sp_defense = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    type1 = models.TextField(blank=True, null=True)
    type2 = models.TextField(blank=True, null=True)
    weight_kg = models.FloatField(blank=True, null=True)
    generation = models.IntegerField(blank=True, null=True)
    is_legendary = models.IntegerField(blank=True, null=True)
    