import re

def matc_l_of_Re(text_chars,list_of_re):

    return [el for el in text_chars if any([re.search(r,el) for r in list_of_re])]

text_chars = ["adccda", "cdaaatdc","??????","atd","abbbbbbdc"]
list_of_re = ["adc","atd"]

print(matc_l_of_Re(text_chars,list_of_re))