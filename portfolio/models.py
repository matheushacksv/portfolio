from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Technologies"


class Project(models.Model):

    class Category(models.TextChoices):
        BACKEND = 'BACKEND', 'Back-end'
        FRONTEND = 'FRONTEND', 'Front-end'
        FULLSTACK = 'FULLSTACK', 'Full-stack'
        DATAIA = 'DATAIA', 'Data & IA'

    name = models.CharField(max_length=255)
    description = models.TextField()    
    techs = models.ManyToManyField(Technology, related_name='projects')
    github = models.URLField(null=True, blank=True)
    demo = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='projects/images/', null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    personal_rating = models.IntegerField(default=0, choices=[(i, i) for i in range(1, 11)])
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.BACKEND)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Experience(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    top_techs = models.ManyToManyField(Technology, related_name='experiences')
    actual = models.BooleanField(default=False)
    image = models.ImageField(upload_to='experiences/images/', null=True, blank=True)

    started_at = models.DateField()
    ended_at = models.DateField(null=True, blank=True) 
    
    
