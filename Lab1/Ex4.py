def lowercase(convert):
    global var
    cuv_nou = []
    for i in convert:
        var = convert
    for i in range(len(convert)):
        cuv_nou.append(convert[i])

        if convert[i].islower() == True and convert[i + 1].isupper() == True:
            convert = convert[:i + 1] + "_" + convert[i + 1:]
            cuv_nou.append(convert)
        if convert[i] == var and convert[i].isupper():
            cuv_nou.append("_")
            cuv_nou.append(convert[i].lower())

    convert = convert.lower()
    return convert


print("The lower case form is: " + str(lowercase('UpperCamelCaseA')))
print("")