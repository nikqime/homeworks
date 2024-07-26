def smaller(arr):
    resoult=[]
    for i in arr:
        spell=0
        for b in arr[i+1:]:
            if b < arr[i]:
                spell += 1
        resoult.append(spell)
    return resoult

#ვერ გავაკეთე ბოლომდე :(