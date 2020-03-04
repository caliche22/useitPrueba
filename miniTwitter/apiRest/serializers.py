from rest_framework import serializers
from .models import Usuario
from .models import Post
### serializarlo para probarloc con postman
class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('name', 'email','alias')
 

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('text')
