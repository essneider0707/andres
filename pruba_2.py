#:)
def multiplo8 (lista):
    for  m in lista :
        mul_8 = 0
        if m % 8 ==0:
            mul_8 = mul_8 + 1
    return mul_8
def mayorMenor0(lista):
    for i in lista:
        ma_0 = 0
        me_0 = 0
    if i > 0:
        ma_0 = ma_0 + 1
    elif i < 0:
        me_0 = me_0 + 1
    return ma_0 , me_0 