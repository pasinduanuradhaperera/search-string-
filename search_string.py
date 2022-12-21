text = input()
word = input()


def search(x, y):
    if len(y) <= len(x):

        for i in range(len(x)-len(y)+1):

            if x[i:len(y)+i] == y:
                return 'Word found'

        return 'Word not found'

    else:
        return 'Word not found'


print(search(text, word))
