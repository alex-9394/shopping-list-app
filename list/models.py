from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']