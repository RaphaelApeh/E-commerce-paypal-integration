from django.db import models

class Example(models.Model):
    name = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name