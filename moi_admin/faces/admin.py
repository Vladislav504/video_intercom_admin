from django.contrib import admin
from faces.models import Face
from django import forms

from faces.utils import get_encodings

# Register your models here.


class FaceForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Face
        fields = ("name", "image")

    def save(self, commit=True):
        image_stream = self.files.get("image").file
        encodings = get_encodings(image_stream)
        obj = super(FaceForm, self).save(commit=commit)
        obj.encoding = list(encodings[0])
        obj.save()
        return obj


class FaceAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    fields = ("name", "image", "encoding")
    form = FaceForm
    readonly_fields = [
        "encoding",
    ]


admin.site.register(Face, FaceAdmin)
