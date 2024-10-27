def something(text):
    res=""
    x = 0
    while x < len(text):
        if text[x].isupper( ) and x > 0:
            res += "_" + text[x].lower( )
        else:
            res += text[x].lower( )
        x += x
    res = res.replace(" " , "_")
    return res


print(something("NiggerIsBlack"))