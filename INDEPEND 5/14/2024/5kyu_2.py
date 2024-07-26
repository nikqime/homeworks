def work_on_strings(a,b):
    for y in b:
        for i in a:
            if i==y:
                y.upper()
            elif y==i:
                i.upper()
    return a+b
                