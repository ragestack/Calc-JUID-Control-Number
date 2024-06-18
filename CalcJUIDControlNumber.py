# -*- coding: utf-8 -*-
#
# Calc JUID Control Number
# Python 3.8.1
#
# Copyright (c) Denis Leonov 466611@gmail.com
#
# УИД - уникальный идентификатор дела, используется в системе ГАС Правосудие и смежных АИС
# Пример полного УИД с КЧ: 01VS0001-01-2020-222222-02
# Структура: {код суда}-{номер здания суда}-{год присвоения УИД}-{порядковый номер}-{контрольное число}
#
# Скрипт находит контрольное число (КЧ), например 02, для идентификатора 01VS0001-01-2020-222222
# Полученный полный УИД с контрольным числом 01VS0001-01-2020-222222-02 проходит успешную проверку на КЧ
#
# ПРИМЕЧАНИЕ и отказ от ответственности:
# Не рекомендуется использовать скрипт для формирования автоматизированных запросов
# Программа предоставляется "как есть", любые явные или подразумеваемые гарантии автора отсутствуют

def calcMod97(code):
    modulus = 97
    maxS = 999999999
    s = 0
    for c in code:
        if c.isdigit():
            a = ord(c) - ord('0')
        elif c.isupper():
            a = ord(c) - ord('A') + 10
        elif c.islower():
            a = ord(c) - ord('a') + 10
        else:
            a = 0

        if a >= 10:
            s = s * 100 + a
        else:
            s = s * 10 + a

        if s > maxS:
            s = s % modulus

    result = s % modulus
    return result

def validateJuid(juid):
    minJuidLen = 2
    code = ''.join(filter(str.isalnum, juid))
    if len(code) < minJuidLen:
        return False
    checksum = code[-2:]
    if checksum in ['00', '01', '99']:
        return False
    if calcMod97(code) == 1:
        return True
    return False

# Функция ищет и добавляет КЧ (контрольное число) к УИД
def addCN(code):
    for i in range(0,100):
        s = code + '-' + str(i).zfill(2)
        if validateJuid(s) == True:
            return s

# Пример использования, где в качестве juid задаётся значение без контрольного числа
_juid = '01VS0001-01-2020-222222'

# Результат нахождения верного КЧ (контрольного числа) и вывод полного УИД
juid = addCN(_juid)
print('juid:',juid,'\nvalid:',validateJuid(juid))


