#3) Remove Duplicates from a List (3 ქულა)
#Create a program that receives a list and removes duplicate elements while maintaining the original order.
#Examples:
#[1, 2, 2, 3, 4, 4, 5] --> [1, 2, 3, 4, 5]
#['a', 'b', 'a', 'c'] --> ['a', 'b', 'c']


def number(x):
    res=[]
    for i in x:
        if i not in res:
            res.append(i)
    return res
list=[14,14,15,16,17,18,30,16]
new_list=number(list)

print(new_list)