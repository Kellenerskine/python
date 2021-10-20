def doThings(word):
    """
    >>> doThings("fishy")
    'fishies'
    >>> doThings("tree")
    'trees'
    >>> doThings("word")
    'words'
    >>> doThings("puppy")
    'puppies'
    >>> doThings("fish")
    'fishs'
    >>> doThings("")
    'nothings'
    """
    if word.endswith("y"):
        return word.replace("y", "ies")
    elif word == "":
        return 'nothings'
    else:
        return word + "s"
