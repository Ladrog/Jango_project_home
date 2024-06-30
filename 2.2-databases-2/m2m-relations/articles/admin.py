from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tag_count = 0
        for form in self.forms:
            cleaned_data = form.cleaned_data
            tag = cleaned_data.get('tag')
            if tag is None:
                raise ValidationError('Укажите раздел')
            if cleaned_data.get('is_main'):
                main_tag_count += 1
            if main_tag_count > 1:
                raise ValidationError('Укажите только один основной раздел')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
