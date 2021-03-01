from django import template

register = template.Library()


@register.filter(name='censor')
def censor(value):
    if isinstance(value, str):
        censor_words = ['плохоеслово', 'компостер', 'гадость', 'лох']
        split_string = value.split()
        for word in censor_words:
            if word in split_string:
                for j in range(len(split_string)):
                    if word == split_string[j]:
                        split_string[j] = '*' * len(split_string[j])
                        # result = ' '.join(split_string)
        return ' '.join(split_string)
    else:
        raise ValueError(f'Ошибка: значение должно быть строкой')



