def reverse_alternate(st):
    splited=st.split()
    for i in range(len(splited)):
        if i % 2 ==1:
            splited[i]=splited[i][::-1]
    result= " ".join(splited)
    return result