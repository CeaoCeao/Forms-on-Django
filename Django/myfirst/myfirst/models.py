from django.db import models

class Insert(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    dod = models.DateField()
    content = models.TextField(max_length=250)
    author = models.CharField(max_length=100)

    class Meta:
        db_table = "obituaries"
