
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

from string import ascii_lowercase
def missingLetter(txt: str) -> str:
    letters = list(ascii_lowercase)
    
    lock = 0
    for i in txt:
        if i in letters:
            index = letters.index(i)
            
            if lock == 0:
                lock += 1
                newindex = index + 1
            
            if index + 1 == newindex:
                newindex += 1
            else:
                return letters[newindex - 1]
            
    return "No Missing Letter"