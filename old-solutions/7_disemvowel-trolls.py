def disemvowel(string_):
    newstring_ = string_
    for vowel in 'aeiouAEIOU':
        newstring_ = newstring_.replace(vowel, "")
    return newstring_