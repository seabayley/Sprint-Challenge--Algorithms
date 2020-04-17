'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    sub = "th"
    x = len(word)
    y = len(sub)

    if x < y:
        return 0

    if word[0: y] == sub:
        return count_th(word[y - 1:]) + 1

    return count_th(word[y - 1:])
