from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class UserRegistration(models.Model):
    Id_Type = models.CharField(max_length=50, choices=[
        ('National ID', 'National ID'),
        ('Passport', 'Passport'),
        ('Alien ID', 'Alien ID'),
    ], default='', verbose_name="National ID"
    )
    Id_Number = models.BigIntegerField()
    Open_Date = models.DateTimeField()
    Title = models.CharField(max_length=10, choices=[
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Ms', 'Ms'),
        ('Other', 'Other'),
    ], default='', verbose_name="Title")
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Birth_Date = models.DateField()
    Kra_Pin = models.BigIntegerField()
    Country = models.CharField(max_length=100)
    County = models.CharField(max_length=100)
    Residence = models.CharField(max_length=100)
    Postal_Code = models.CharField(max_length=100)
    Mobile = models.BigIntegerField()
    Email = models.EmailField()
    Password = models.CharField(max_length=100)

    def set_Password(self, raw_Password):
        """Hash the password and store it."""
        self.Password = make_password(raw_Password)

    def check_password(self, raw_Password):
        """Check if the provided password matches the stored hashed password."""
        return check_password(raw_Password, self.Password)

    def __str__(self):
        return self.Email
    
class Contact(models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100) 
    Email = models.EmailField(max_length=100)
    Mobile = models.BigIntegerField()   
    Message = models.TextField()

    def __str__(self):
        return self.Email

class Transaction(models.Model):
    Transaction_type = models.CharField(max_length=10, choices=[
        ('1', 'Deposit'),
        ('2', 'Withdrawal'),
        ('3','Other')
    ],default='', verbose_name='Transaction')    
    Amount = models.BigIntegerField()
    Date = models.DateTimeField()

    def __str__(self):
        return self.Transaction_type