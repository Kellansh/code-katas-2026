def get_count(sentence):
    count = 0
    for char in sentence:
        if (char in ["a", "e", "i", "o", "u"]):
            count += 1
    return count

print(get_count("hello world"))