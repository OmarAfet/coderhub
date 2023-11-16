def int_to_roman(num: int) -> str:
    roman = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
    result = ""
    for i in roman.keys():
        result += roman[i] * (num // i)
        num = num % i
    return result


print(int_to_roman(1))  # I
print(int_to_roman(2))  # II
print(int_to_roman(6))  # VI
print(int_to_roman(23))  # XXIII


"""
https://coderhub.sa/challenges/802acf2a-5e56-42ca-b517-9e482e127359/view?activity_id=f5d29099-50fe-424c-976f-c625d5636ef3&language=Python&canChangeLanguage=true

الأعداد الرومانية
20 نقطة لكل لغة
صعب
وصف التحدي
اكتب دالة تستقبل عددًا صحيحًا موجبًا int وتحوله إلى تمثيله بالأرقام الرومانية

العدد بالرومانية	العدد	العدد بالرومانية	العدد
XC	90	I	1
C	100	IV	4
CD	400	V	5
D	500	IX	9
CM	900	X	10
C	1000	XL	40
L	50		
المخرجات المتوقعة
الاختبار 1

المدخلات (Inputs)
num = 1
المخرجات (Outputs)
'I'
الاختبار 2

المدخلات (Inputs)
num = 2
المخرجات (Outputs)
'II'
الاختبار 3

المدخلات (Inputs)
num = 6
المخرجات (Outputs)
'VI'
الاختبار 4

المدخلات (Inputs)
num = 23
المخرجات (Outputs)
'XXIII'
"""
