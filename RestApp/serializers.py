from rest_framework import serializers

from RestApp.models import (
    Author,
    Book,
    Login,
)

# class LoginSerializer(serializers.Serializer):
#       username= serializers.CharField(max_length=30)
#       password = serializers.CharField(max_length=30)
#
#
#       def restore_object(self, attrs, instance=None):
#            if instance is not None :
#                instance.username=attrs.get('username',instance.username)
#                instance.password=attrs.get('password',instance.password)
#                return instance
#            else :
#                return Login(**attrs)
from RestApp.models import Login

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('username', 'password')

        def restore_object(self, attrs, instance=None):

            if instance:
                 instance.username = attrs.get('username', instance.title)
                 instance.password= attrs.get('password', instance.code)
                 return instance
            return Login (**attrs)


from django.forms import widgets
from rest_framework import serializers
from RestApp.models import Snippet


class SnippetSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    title = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=100000)
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(default='python')
    style = serializers.ChoiceField(default='friendly')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.title = attrs.get('title', instance.title)
            instance.code = attrs.get('code', instance.code)
            instance.linenos = attrs.get('linenos', instance.linenos)
            instance.language = attrs.get('language', instance.language)
            instance.style = attrs.get('style', instance.style)
            return instance

        # Create new instance
        return Snippet(**attrs)