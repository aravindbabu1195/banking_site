from django.db import models

class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Registration(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    ACCOUNT_TYPE_CHOICES = (
        ('Savings', 'Savings Account'),
        ('Current', 'Current Account'),
    )

    MATERIAL_CHOICES = (
        ('Debit Card', 'Debit Card'),
        ('Credit Card', 'Credit Card'),
        ('Cheque Book', 'Cheque Book'),
    )

    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES)
    materials_provide = models.ManyToManyField('Material', blank=True)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
