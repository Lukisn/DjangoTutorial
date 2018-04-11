from django.contrib import admin
from .models import Publisher, Author, Book
# iniital superuser: admin, ihavecowpowers


class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "state_province", "country", "website")
    list_filter = ("country", "state_province", "city")
    search_fields = ("name", )


admin.site.register(Publisher, PublisherAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "first_name", "last_name", "email")
    search_fields = ("first_name", "last_name")


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    # admin form customization:
    # fields = []  # entry field ordering
    # fieldsets = [(, {"fields": []})]  # entry field grouping
    # inlines = []  # inline model entries
    # change list customization:
    list_display = ("title", "publisher", "publication_date")
    list_filter = ("publisher", "publication_date")
    search_fields = ("title", )


admin.site.register(Book, BookAdmin)

