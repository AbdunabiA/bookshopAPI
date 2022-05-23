from django.shortcuts import render
from rest_framework import authentication, permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import BookSerializer, ReviewSerializer, SocialMediaSerializer, TermsOfTradeSerializer, AddsSerializer, BookmarkSerializer, CategorySerializer
from .models import Book, Review, SocialMedia, TermsOfTrade, Adds, Bookmark, Category
from django_filters import rest_framework as filters
from rest_framework.views import APIView
class CategoryFilter(filters.FilterSet):
    make = filters.ModelChoiceFilter(field_name="category__title", to_field_name='title', queryset=Category.objects.all())

    class Meta:
        model = Book
        fields = ('category',)
class BookGetAll(ListAPIView):
    search_fields = ['title', 'author',]
    ordering_fields = ['sellingPrice', 'category', 'sellCount', 'searchCount']
    filter_backends = (SearchFilter, OrderingFilter, filters.DjangoFilterBackend,)
    category = CategorySerializer
    filter_class = CategoryFilter
    serializer_class = BookSerializer
    def get_queryset(self):
        books = Book.objects.all()
        soz = self.request.query_params.get("search")
        if soz is not None:
            books = Book.objects.filter(title__contains=soz)
            for i in books:
                i.searchCount = i.searchCount + 1
                i.save()
        return books
class BookGet(RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class ReviewGetAll(ListAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
class ReviewGet(RetrieveAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

class SocialMediaGetAll(ListAPIView):
    serializer_class = SocialMediaSerializer
    queryset = SocialMedia.objects.all()
class SocialMediaGet(RetrieveAPIView):
    serializer_class = SocialMediaSerializer
    queryset = SocialMedia.objects.all()

class TermsOfTradeGetAll(ListAPIView):
    serializer_class = TermsOfTradeSerializer
    queryset = TermsOfTrade.objects.all()
class TermsOfTradeGet(RetrieveAPIView):
    serializer_class = TermsOfTradeSerializer
    queryset = TermsOfTrade.objects.all()

class AddsGetAll(ListAPIView):
    serializer_class = AddsSerializer
    queryset = Adds.objects.all()
class AddsGet(RetrieveAPIView):
    serializer_class = AddsSerializer
    queryset = Adds.objects.all()

class BookmarkGetAll(ListAPIView):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()
class BookmarkGet(RetrieveAPIView):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()

class CategoryGetAll(ListAPIView):
    ordering_fields = ['title']
    filter_backends = (OrderingFilter,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
class CategoryGet(RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
