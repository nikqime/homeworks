#1) Binary --> Decimal Conversion (2 ქულა)

#Create a program which receives a binary number and converts it to decimal.

#Examples:
#10001 --> 17
#1111 --> 15
def Binary(n):
    part_1=0
    part_2=0
    for i in n[::-1]:
        if i == '1':
            part_1 += 2 ** part_2
        part_2 += 1
    return part_1

n='101010101010101111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111011111110010101010101001010101010101'
print(Binary(n))



