import re

def Split_It(S):
    Regexsplit=re.compile('(\s*\w+\s*)')
    Words = []
    for word in Regexsplit.findall(S):
        if word[0] == ' ':
            word = word[1:]
        if word[-1] == ' ':
            word = word[:-1]
        word.replace(' ','')
        Words.append(word)
    return Words;

S = "alma armud heyva qarpız 2"
Splitedwords = Split_It(S)
for word in Splitedwords:
    print(word,end=' ')