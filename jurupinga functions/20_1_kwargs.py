def media(*args):
    notas = 0
    for nota in args:
        notas+=nota
    return notas / len(args)


print(media(100, 50))
