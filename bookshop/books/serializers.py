from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.core.exceptions import ValidationError
from .models import *

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    def validate_title(self, value):
        if len(value) <=2:
            raise ValidationError("Kitob nomi 2ta harfdan kop bo'lishi kerak")


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class SocialMediaSerializer(ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'

class TermsOfTradeSerializer(ModelSerializer):
    class Meta:
        model = TermsOfTrade
        fields = '__all__'

class AddsSerializer(ModelSerializer):
    class Meta:
        model = Adds
        fields = '__all__'

class BookmarkSerializer(ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model =Category
        fields = '__all__'