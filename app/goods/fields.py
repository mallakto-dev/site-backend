from transliterate import translit
from rest_framework.fields import Field


class SlugField(Field):

    def to_internal_value(self, data):
        return str(data)

    def to_representation(self, value):
        return "-".join(
            translit(value.lower(), "ru", reversed=True).split()
        ).replace('"', "")
