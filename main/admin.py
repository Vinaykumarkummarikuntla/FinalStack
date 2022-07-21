"importing packages"
from django.contrib import admin
from .models import *


class QuestionAdmin(admin.ModelAdmin):
    "create a QuestionAdmin class for to view database in admin pages"
    list_display = ('title', 'user')
    search_fields = ('title', 'detail')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)


class CommentAdmin(admin.ModelAdmin):
    "create a CommentAdmin class for to view database in admin pages"
    list_display = ('answer', 'comment')


admin.site.register(Comment, CommentAdmin)


class UpvoteAdmin(admin.ModelAdmin):
    "create a UpvoteAdmin class for to view database in admin pages"
    list_display = ('answer', 'user')


admin.site.register(UpVote, UpvoteAdmin)


class DownvoteAdmin(admin.ModelAdmin):
    "create a UpvoteAdmin class for to view database in admin pages"
    list_display = ('answer', 'user')


admin.site.register(DownVote, DownvoteAdmin)

admin.site.register(CustomUser)
