def hide_fields(model, remove):
    '''
        Recebe um django.db.models.Model `model` e uma lista de argumentos `remove`.

        Retorna uma lista de todos os argumentos de `model` sem os argumentos em `remove`
    '''

    return [x for x in list(map(lambda x: str(x)[str(x).rfind('.')+1:], model._meta.fields)) if x not in remove]