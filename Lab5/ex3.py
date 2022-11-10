def vowels(string):

    def vowels_with_f(string):

        return [ch for ch in string if ch.lower() in "aeiou"]

    anon_function = lambda string: [ch for ch in string if ch.lower() in "aeiou"]

    first_list = vowels_with_f(string)

    second_list = anon_function(string)

    f_filter = lambda string: list(filter(lambda x: x.lower() in "aeiou", string))

    third_list = f_filter(string)

    return first_list, second_list, third_list

print(vowels("Programming in python is fun"))