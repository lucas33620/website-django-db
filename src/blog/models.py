from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=36)
    slug = models.SlugField()


class BlogPost(models.Model):
    """La clé primaire sera généré automatiquement par Django "pk" """
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # Spécifier le comportement si User venait à être supprimé
    category = models.ManyToManyField(Category) #Lien plusieurs à plusieurs
    title = models.CharField(max_length=128) # Créer un champs de type CharField de longueur 128
    slug = models.SlugField() # Afficher le titre dans l'URL "x-x-x..."
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null = True) # Formulaire peut être vide et permet de stocker une valeur Null correspondant à une autre Type ou Rien 
    content = models.TextField(blank=True)
    description = models.TextField()

    @property # Permet d'enlever les parenthèses
    def publish_string(self):
        if self.published:
            return "L'article est publié"
        return "L'article n'est pas publié"
    
    def save(self, *args, **kwargs): # arguments dans le cli
        
        # automatisation du slug en fonction du titre à chaque sauvegarde
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
