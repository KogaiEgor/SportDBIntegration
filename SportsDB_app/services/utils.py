from django.db import models
from django.core.exceptions import ValidationError


def transform_url(url):
    if not url.startswith(("http://", "https://")):
        return f"https://{url}"
    return url


def fill_model_with_validation(model_class, data):
    model_instance = model_class()
    for field in model_instance._meta.get_fields():
        if not field.concrete or isinstance(field, models.ForeignKey):
            continue

        if field.name in data:
            raw_value = data[field.name]
            if isinstance(field, models.URLField):
                if not raw_value:
                    raw_value = None
                else:
                    raw_value = transform_url(raw_value)
            try:
                cleaned_value = field.clean(raw_value, model_instance)
                setattr(model_instance, field.name, cleaned_value)
            except ValidationError as e:
                print(f"Ошибка преобразования поля {field.name}: {e}")
    return model_instance
