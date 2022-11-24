import re

def regexstr(r,text,x):
    """
    Write a function that receives as a parameter a regex string,
    a text string and a whole number x
    :return: those long-length x substrings that match the regular expression
    """
    return list(filter(lambda el:len(el)==x, re.findall(r,text)))

r = 'adc'
text = 'adc cd adcff '
x=3

print(regexstr(r,text,x))

