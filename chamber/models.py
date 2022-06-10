from django.db import models


class Profile(models.Model):
    BLOOD_GROUP = (
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('OB+', 'OB+'),
        ('OB-', 'OB-')
    )

    MARITAL_STATUS = (
        ('Married', 'Married'),
        ('Unmarried', 'Unmarried'),
    )

    book_no = models.CharField(max_length=10)
    hiveid = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=254)
    address = models.CharField(max_length=254, null=True, blank=True)
    father_name = models.CharField(max_length=254, null=True, blank=True)
    mother_name = models.CharField(max_length=254, null=True, blank=True)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS)
    spouse_name = models.CharField(max_length=254, null=True, blank=True)
    age = models.DateField()
    blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP)
    occupation = models.CharField(max_length=254, null=True, blank=True)
    contact_person = models.CharField(max_length=254, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)

    def __str__(self):
        return str(self.id) + '. ' + self.name


class Prescription(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='prescription/image/', blank=True, null=True)
    pdf = models.FileField(upload_to='prescription/pdf', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='created_by', null=True, blank=True)

    def __str__(self):
        return self.profile.name + ' - ' + str(self.id)
