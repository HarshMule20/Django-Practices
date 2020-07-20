from django.db import models


class Register(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    profile_photo = models.TextField()
    gender = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=10)
    address_1 = models.TextField()
    address_2 = models.TextField()
    dob = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin_code = models.CharField(max_length=10)

    def __str__(self):
        return self.name + ' ' + self.surname
