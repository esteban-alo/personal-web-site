from django.db import models


# Create your models here.
class Project(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects')
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        # Metadata for model
        ordering = ['-created_date']  # Reversed order

    def __str__(self):
        return self.title

