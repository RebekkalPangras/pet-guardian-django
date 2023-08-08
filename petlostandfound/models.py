from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Pet(models.Model):
    GENDER_CHOICES = [('F', 'Female'), ('M', 'Male'), ('UK', 'Unknown')]
    PET_TYPE_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100, blank=True, null=True)
    age = models.PositiveIntegerField(null=True)
    pet_type = models.CharField(max_length=50, choices=PET_TYPE_CHOICES)
    breed = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=True, null=True)
    color = models.CharField(max_length=50)
    owner = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class LostPetReport(models.Model):
    reported_by = models.ForeignKey('User', on_delete=models.CASCADE)
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE)
    report_date = models.DateField()
    last_seen_location = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    is_found = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pet.name} - {self.last_seen_location}"
