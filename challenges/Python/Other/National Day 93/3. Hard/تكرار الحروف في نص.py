def character_count(word: str) -> str:
    word = sorted(word.lower())
    result = ''
    for i in range(len(word)):
        if i == 0:
            result += word[i] + str(word.count(word[i]))
        elif word[i] != word[i - 1]:
            result += word[i] + str(word.count(word[i]))
    return result


print(character_count('aabbbcccc'))
print(character_count('abc'))
print(character_count('Hello'))
print(character_count('aabbcc'))


"""
https://coderhub.sa/challenges/6848a2f5-01b8-478f-a9a3-e2936afff818/view?activity_id=f5d29099-50fe-424c-976f-c625d5636ef3&language=Python

تكرار الحروف في نص
20 نقطة لكل لغة
صعب
وصف التحدي
اكتب دالة function تستقبل نص string و تقوم بإرجاع كل حرف وعدد تكراره بالترتيب الأبجدي .

المخرجات المتوقعة
الاختبار 1

المدخلات (Inputs)
word = 'aabbbcccc'
المخرجات (Outputs)
'a2b3c4'
الاختبار 2

المدخلات (Inputs)
word = 'abc'
المخرجات (Outputs)
'a1b1c1'
الاختبار 3

المدخلات (Inputs)
word = 'Hello'
المخرجات (Outputs)
'e1h1l2o1'
الاختبار 4

المدخلات (Inputs)
word = 'aabbcc'
المخرجات (Outputs)
'a2b2c2'
"""
