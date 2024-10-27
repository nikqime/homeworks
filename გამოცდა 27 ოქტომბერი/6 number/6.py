#6) Convert Pascal Case string into snake_case (4 ქულა)

#You will receive a string which will contain words in PascalCase, your job is to convert them into snake_case.

#Examples:
#"TestController"  -->  "test_controller"
#"MoviesAndBooks"  -->  "movies_and_books"
#"App7 Test"       -->  "app7_test"
#1                 -->  "1"
def something(text):
    res=""
    x = 0
    while x < len(text):
        if text[x].isupper( ) and x > 0:
            res += "_" + text[x].lower()  
        else:
            res += text[x].lower()
        x += 1
    res = res.replace(" " , "_")
    return res


print(something("IDontLikeSchool"))