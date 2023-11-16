def perfect_Number_check(num: int) -> bool:
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False


"""
https://coderhub.sa/challenges/ab2b2c46-831a-47be-bd87-ec91b7176e36/view?activity_id=f5d29099-50fe-424c-976f-c625d5636ef3&language=Python&canChangeLanguage=true

التحقق من الرقم المثالي
10 نقاط لكل لغة
متوسط
وصف التحدي
اكتب دالة function تستقبل عددًا صحيحًا موجبًا int وتحدد ما إذا كان عددًا مثاليًا أم لا. العدد المثالي يساوي مجموع قواسمه الصحيحة (باستثناء الرقم نفسه).

المخرجات المتوقعة
الاختبار 1

المدخلات (Inputs)
num = 6
المخرجات (Outputs)
true
الاختبار 2

المدخلات (Inputs)
num = 28
المخرجات (Outputs)
true
الاختبار 3

المدخلات (Inputs)
num = 12
المخرجات (Outputs)
false
الاختبار 4

المدخلات (Inputs)
num = 14
المخرجات (Outputs)
false
"""
