from transliterate import translit


def slugify_name(name):
    return "-".join(
        translit(name.lower(), "ru", reversed=True).split()
    ).replace('"', "")
