from django.apps import AppConfig


class WordofmouthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wordofmouth'

class PostsConfig(AppConfig):
    name = 'posts'