from django.contrib.auth.models import User
from django.db import models


class Party(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    code = models.IntegerField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Parties'

    def __str__(self):
        return f'{self.name}'


class Vote(models.Model):
    user = models.ForeignKey(User, related_name='vote', on_delete=models.CASCADE)
    party = models.ForeignKey(Party, related_name='votes', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'{self.user.pk} - {self.party.name}'
