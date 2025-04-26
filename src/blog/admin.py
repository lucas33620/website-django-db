from django.contrib import admin
from blog.models import BlogPost

# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    # Ajouter les colonnes sur l'interface
    list_display = (
        "title",
        "slug", 
        "published",
        "author",
        "date",
        "number_of_words",
    )

    # Remplacer les champs vides qui n'est pas possible ManyToManyField
    empty_value_display = " "

    # Indiquer les champs éditable par des tuples (penser à la virgule)
    list_editable = ("title", "published", )
    list_display_links = ("slug", ) # Champs cliquable poru accéder à l'article (default = title)
    search_fields = ("title", "author__username", ) # Champs de recherche appliqué (attention aux ForeignKey comme author)
    list_filter = ("published", "author",) # Champs de filtre
    autocomplete_fields = ("author", ) # Pouvoir écrire du texte sur les champs d'un article au lieu de menu déroulant
    list_per_page = 10 # Permet de limiter le nombres d'articles par page permet de fluidifier l'administration