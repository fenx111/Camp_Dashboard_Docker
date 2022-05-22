from rest_framework import serializers
from .models import Children

class SelectChildrens(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = ['last_name', 'first_name']