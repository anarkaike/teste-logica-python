# coding: utf-8
# 1) Crie uma função que retorna o maior número ímpar da sequência (sem usar max).
# Exemplo: fn([1,2,3,4,5,6,7,8,19,10,1,12,14,16 m])
def my_max(arr):
    max_num = False
    for num in arr:
        if num % 2 != 0 and (False == max_num or num > max_num):
            max_num = num
    return max_num

max_num = str(my_max([1, 2, 3, 4, 5, 6, 7, 8, 19, 10, 11, 12, 14, 16]))
print("O maior número da sequencia é: {0}".format(max_num))