from django import forms
from .models import BlogPost


# class CreatePostForm(forms.Form):
#     title = forms.CharField(max_length=25, required=True)
#     content = forms.CharField(max_length=250, required=True, widget=forms.Textarea)
#     slug = forms.SlugField(max_length=25, required=True)


class CreatePostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'slug', 'content', 'publish_date']

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__iexact=title) # iexact -> нечувствительность к регистру заголовка
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("Этот заголовок уже используется. Выберите другой.")
        return title
