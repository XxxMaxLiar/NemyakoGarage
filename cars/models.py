from django.db import models

class Car(models.Model):
    number = models.IntegerField(help_text="Номер Машины")
    make = models.CharField(help_text="Фирма Машины", max_length = 50)
    color = models.CharField(max_length = 51)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.number} {self.make} {self.color}"
