from django.contrib import admin

from .models import Book, SocialMedia, TermsOfTrade, Review, Adds, Bookmark, Category

admin.site.register(Book)
admin.site.register(SocialMedia)
admin.site.register(TermsOfTrade)
admin.site.register(Review)
admin.site.register(Adds)
admin.site.register(Bookmark)
admin.site.register(Category)
