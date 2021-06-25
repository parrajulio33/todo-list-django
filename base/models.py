from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    jira_title = models.CharField(max_length=200)
    done_yesterday = models.TextField(null=True, blank=True)
    doing_today = models.TextField(null=True, blank=True)
    any_blocker = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.jira_title

    class Meta:
        ordering = ['complete']