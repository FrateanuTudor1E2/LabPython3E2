import re

def censor(s):
    low_s = s.group(0).lower()
    if not (low_s[0] in "aeiou" and low_s[-1] in "aeiou"):
        return s.group(0)
    return "".join([ch if idx%2 == 0 else '*' for idx,ch in enumerate(s.group(0))])


def censorship(text):
    return re.sub("\w+",censor,text)

text= "ana mananca mere"

print(censorship(text))