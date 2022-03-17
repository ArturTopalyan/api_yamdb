from django.contrib.auth import get_user_model
from rest_framework  import serializers
from rest_framework.generics import get_object_or_404

from .models import Genre

User = get_user_model()


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ['id']