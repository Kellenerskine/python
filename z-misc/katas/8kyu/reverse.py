def reverse_words(text):
    input = text
    result = []
    for i in input:
        while i != " ":
            result.insert(0, i)
        result.append(" ")

    return str(result)
