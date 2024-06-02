from django.contrib import admin
from books.models import Book, Comment

class BookModelAdmin(admin.ModelAdmin):
    list_display = (
        "book_name",
        "writer",
        "description",
        "published_date",
        "created_date",
        "updated_date",
    )

class CommentModelAdmin(admin.ModelAdmin):
    list_display = (
        "get_book_name",
        "owner_of_comment",
        "comment",
        "created_date",
    )

    def get_book_name(self, obj):
        return obj.book.book_name
    get_book_name.short_description = 'Book Name'

admin.site.register(Book, BookModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
