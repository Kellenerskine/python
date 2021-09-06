def plural_of(word):
    """Returns the plural of the word.
    >>> plural_of("word")
    'words'
    >>> plural_of("penny")
    'pennies'
    """

    if word.endswith("y"):
        return word[:-1] + "ies"
    else:
        return word + "s"


if __name__ == "__main__":
    import doctest
    doctest.testmod()