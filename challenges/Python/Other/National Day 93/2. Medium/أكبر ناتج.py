def expression(num1: int, num2: int, num3: int) -> int:
    max = 0
    if num1 + num2 + num3 > max:
        max = num1 + num2 + num3
    if num1 * num2 * num3 > max:
        max = num1 * num2 * num3
    if (num1 + num2) * num3 > max:
        max = (num1 + num2) * num3
    if num1 * (num2 + num3) > max:
        max = num1 * (num2 + num3)
    if num1 * num2 + num3 > max:
        max = num1 * num2 + num3
    if num1 + num2 * num3 > max:
        max = num1 + num2 * num3
    return max

"""
https://coderhub.sa/challenges/a7522ca2-1806-4b26-9bbb-7f75ed4c02ea/view?activity_id=f5d29099-50fe-424c-976f-c625d5636ef3&language=Python

أكبر ناتج
10 نقاط لكل لغة
متوسط
وصف التحدي
قم بكتابة دالة function تستقبل ٣ اعداد صحيحة int المهمة هي إدراج علامات العمليات + و * وربما أقواس بين الأرقام بحيث تكون قيمة الناتج كبيرة قدر الإمكان.

لنفترض مثالاً: الاعداد هي 1 و 2 و 3 فيما يلي بعض طرق وضع العلامات والأقواس:

1 + 2 * 3 = 7

1 * (2 + 3) = 5

1 * 2 * 3 = 6

(1 + 2) * 3 = 9

أكبر ناتج هو 9

المخرجات المتوقعة
الاختبار 1

المدخلات (Inputs)
num1 = 1
num2 = 2
num3 = 3
المخرجات (Outputs)
9
الاختبار 2

المدخلات (Inputs)
num1 = 1
num2 = 3
num3 = 2
المخرجات (Outputs)
8
الاختبار 3

المدخلات (Inputs)
num1 = 3
num2 = 4
num3 = 2
المخرجات (Outputs)
24
الاختبار 4

المدخلات (Inputs)
num1 = 5
num2 = 2
num3 = 1
المخرجات (Outputs)
15
"""
