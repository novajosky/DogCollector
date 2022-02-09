from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Dog(models.Model):
    #define the fields/colums
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    #there will be a feeding set related-manager 
    # used to access a cats feedings

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})

class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=[0][0]
    )

    dog = models.ForeignKey(
        Dog, 
        on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"