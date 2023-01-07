
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def numToEng(n: int) -> str:
    digits = ["zero", "one", "two", "three", "four",
              "five", "six", "seven", "eight", "nine"]

    tens = ["", "", "twenty", "thirty", "forty",
            "fifty", "sixty", "seventy", "eighty", "ninety"]

    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    result = ""

    if n == 0:
        return "zero"

    if n >= 100:
        result += digits[n // 100] + " hundred "
        n %= 100

    if n >= 10:
        if n < 20:
            result += teens[n - 10]
        else:
            if digits[n % 10] == "zero":
                result += tens[n // 10]
            else:
                result += tens[n // 10] + "-" + digits[n % 10]
                
    else:
        result += digits[n]

    return result