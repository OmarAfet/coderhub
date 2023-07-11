
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

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