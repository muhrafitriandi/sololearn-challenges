signs = [input() for i in range(4)]
hasPalindrome = any(map(lambda w: w == w[::-1], signs))
if hasPalindrome:
    print('Open')
else:
    print('Trash')
