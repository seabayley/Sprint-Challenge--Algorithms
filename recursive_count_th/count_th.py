'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    return 0 if len(word) < 2 else count_th(word[1:]) + 1 if word[0:2] == 'th' else count_th(word[1:])
