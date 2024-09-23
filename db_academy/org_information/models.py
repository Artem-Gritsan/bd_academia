
from django.db import models


class Organizations(models.Model):
    org_name = models.TextField(primary_key=True)
    org_type = models.TextField()
    web_site = models.TextField()
    director = models.TextField()
    phone_number = models.TextField()
    org_structure = models.TextField()
    org_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'organizations'
