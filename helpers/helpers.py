from random_word import RandomWords
import random

"""
Soup helpers module
"""

r = RandomWords()

col = 0
row = 0
col2 = 0
row2 = 0
sc = 0
word = ""


# Define matrix creation
def word_soup_create(col, row):

    return [["*" for x in range(0,col)] for y in range(0,row)]

# Replace every element in matrix with random letters form "a" to "z"
def word_soup_randomize(matrix, col, row):
    for i in range (0,row):
        for j in range (0,col):
            matrix[i][j]=chr(random.randint(97,122))
    return matrix

# Inserts a horizontal word, from left to right
def word_soup_addltr(matrix, col, row):

    soup_data = {
        "matrix" : matrix,
        "word" : []
    }

    word = r.get_random_word(hasDictionaryDef="true", maxLength=8)
    word = word.lower()
    row2 = random.randint(0,row)
    col2 = random.randint(0, (col-len(word)))
    for c in word:
        matrix[row2][col2] = c
        col2 += 1
    soup_data["word"].append(word)

    return soup_data

# Inserts a vertical word, from top to bottom
def word_soup_addttb(matrix, col, row):

    soup_data = {
        "matrix" : matrix,
        "word" : []
    }

    word = r.get_random_word(hasDictionaryDef="true", maxLength=8)
    word = word.lower()
    row2 = random.randint(0, (row-len(word)))
    col2 = random.randint(0, col)

    for c in word:
        matrix[row2][col2] = c
        row2 += 1

    soup_data["word"].append(word)

    return soup_data
