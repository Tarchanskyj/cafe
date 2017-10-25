from django.contrib import admin
from apps.tables.models import Hall, Table
from django import forms

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('number', 'shape', 'x', 'y', 'length', 'width', 'hall')

    def clean(self):
        form = self.cleaned_data
        if form['x'] == form['y']:
            raise forms.ValidationError("X and Y must be not equal!!!")
        return self.cleaned_data


class TableAdmin(admin.ModelAdmin):
    form = TableForm
    list_display = ('number', 'shape', )


admin.site.register(Table, TableAdmin)
admin.site.register(Hall)

# Register your models here.
