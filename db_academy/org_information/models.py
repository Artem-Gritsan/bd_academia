
from django.db import models


# class Organizations(models.Model):
#     org_name = models.TextField(primary_key=True)
#     org_type = models.TextField()
#     web_site = models.TextField()
#     director = models.TextField()
#     phone_number = models.TextField()
#     org_structure = models.TextField()
#     org_id = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'organizations'


class Organizations(models.Model):
    org_name = models.CharField(max_length=200, unique=True)
    org_type = models.CharField(max_length=200)
    website = models.CharField(max_length=200, null=True)
    director = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50, null=True)
    org_structure = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True)
    activity_type = models.CharField(max_length=1000, null=True)

    class Meta:
        db_table = 'organizations_2'