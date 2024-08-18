def multiply_all(arr):
    def multiply_by(n):
        result=[]
        for i in arr:
            result.append(i*n)
        return result
    return multiply_by
    