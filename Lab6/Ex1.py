import re
def words(text):

    return re.findall("[a-z0-9]+",text,flags=re.IGNORECASE)

print(words("adc a6t ttt abc3 attc ////// ????? 123"))