from django.contrib import admin
from django.urls import path, include
from books.views import BookGetAll, BookGet, ReviewGetAll,ReviewGet, SocialMediaGetAll, SocialMediaGet, TermsOfTradeGetAll, TermsOfTradeGet, AddsGetAll, AddsGet, BookmarkGetAll, BookmarkGet, CategoryGetAll, CategoryGet
from rest_framework.routers import DefaultRouter
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookGetAll.as_view(), name='books'),
    path('book/<int:pk>', BookGet.as_view(), name='book'),
    path('reviews/', ReviewGetAll.as_view(), name='reviews'),
    path('review/<int:pk>', ReviewGet.as_view(), name='review'),
    path('socialmedias/', SocialMediaGetAll.as_view(), name='socialmedias'),
    path('socialmedia/<int:pk>', SocialMediaGet.as_view(), name='socialmedia'),
    path('termsoftrades/', TermsOfTradeGetAll.as_view(), name='termsoftrades'),
    path('termsoftrade/<int:pk>', TermsOfTradeGet.as_view(), name='termsoftrade'),
    path('adds/', AddsGetAll.as_view(), name='adds'),
    path('add/<int:pk>', AddsGet.as_view(), name='add'),
    path('bookmarks/', BookmarkGetAll.as_view(), name='bookmarks'),
    path('bookmark/<int:pk>', BookmarkGet.as_view(), name='bookmark'),
    path('categories/', CategoryGetAll.as_view(), name='categories'),
    path('category/<int:pk>', CategoryGet.as_view(), name='category'),
    path('users/', include('users.urls')),
]
