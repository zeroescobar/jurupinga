def media(*args, list=[]):
    total = 0
    if not list:
        for num in args:
            total += num
        fator = len(args)
        return total / fator
    elif list:
        for item in list:
            total += item
        fator = len(list)
        return total / fator
