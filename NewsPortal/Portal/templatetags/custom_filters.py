from django import template

register = template.Library()


# Делаем фильтр для отображения в представления запрещенных слов
# регистрируем его
@register.filter()
def censor(value: str):
    # Список запрещенных слов
    forbidden = ['запорожской']
    # ну а тут должно быть все понятно
    for _ in value.split():
        if _.isalpha() and _.lower() in forbidden:
            # Если слово попадается оставляем первую букву остальные делаем звездочки
            value = value.replace(_, f'{_[0]}{"*" * (len(_) - 1)}')

    return value