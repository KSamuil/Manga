from django import forms
from . import models, parser

class ParserMangaForm(forms.Form):
    MEDIA_CHOISCES = (
        ('manga.kg', 'manga.kg'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOISCES)

    class Meta:
        fields = [
            'media_type',
        ]
    def parser_data(self):
        if self.data['media_type'] == 'manga.kg':
            manga_parser = parser.parser()
            for i in manga_parser:
                models.Remanga.objects.create(**i)