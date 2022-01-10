# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 23:23:59 2020

@author: Gerardo Romero
"""
# def getGuessedWord(secretWord, lettersGuessed):
#     '''
#     secretWord: string, the word the user is guessing
#     lettersGuessed: list, what letters have been guessed so far
#     returns: string, comprised of letters and underscores that represents
#       what letters in secretWord have been guessed so far.
#     '''
# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']  
# tryOut=[]
# # tryOut=len(secretWord)*'_ '
# for k in secretWord:
#     tryOut.append('_ ')
# showMe=list(secretWord)
# for letter in lettersGuessed:
#     if letter in showMe:
#         while letter in showMe:
#             i=showMe.index(letter)
#             showMe.remove(letter)
#             showMe.insert(i,0)
#             del(tryOut[i])
#             tryOut.insert(i,letter)
# tryOut=''.join(tryOut)
# print(tryOut)        

# def getGuessedWord(secretWord, lettersGuessed):
#     '''
#     secretWord: string, the word the user is guessing
#     lettersGuessed: list, what letters have been guessed so far
#     returns: string, comprised of letters and underscores that represents
#       what letters in secretWord have been guessed so far.
#     '''
#     tryOut=[]
#     for k in secretWord:
#         tryOut.append('_ ')
#     showMe=list(secretWord)
#     for letter in lettersGuessed:
#         if letter in showMe:
#             while letter in showMe:
#                 i=showMe.index(letter)
#                 showMe.remove(letter)
#                 showMe.insert(i,0)
#                 del(tryOut[i])
#                 tryOut.insert(i,letter)
#     tryOut=''.join(tryOut)
#     return(tryOut) 

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getGuessedWord(secretWord, lettersGuessed))

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alfabet=string.ascii_lowercase
    list_abc=list(alfabet)
    for i in lettersGuessed:
        if i in list_abc:
            list_abc.remove(i)
    list_abc=''.join(list_abc)
    return(list_abc)

print(getAvailableLetters(lettersGuessed))
#     showMe=[]
#     for letter in secretWord:
#         showMe.append(letter)
#     return(showMe)
    
  
# print(getGuessedWord(secretWord, lettersGuessed))



# def isWordGuessed(secretWord, lettersGuessed):
#     '''
#     secretWord: string, the word the user is guessing
#     lettersGuessed: list, what letters have been guessed so far
#     returns: boolean, True if all the letters of secretWord are in lettersGuessed;
#       False otherwise
#     '''
#     condition=0
#     for letter in secretWord:
#         if letter not in lettersGuessed:
#             condition+=1
#     if condition == 0:
#         return True
#     else:
#         return False


# # secretWord = 'apple' 
# # #lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# # lettersGuessed = ['e', 'l', 'p', 'p', 'a', 'a']
# print(isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
# print(isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
# print(isWordGuessed('carrot', ['c', 'w', 'y', 'j', 'd', 'p', 'q', 'e', 'o', 'i']))
# print(isWordGuessed('lettuce', ['d', 'b', 'k', 'c', 'l', 'e', 'h', 'u', 'f', 'j']))
# print(isWordGuessed('lettuce', []))
# print( isWordGuessed('mangosteen', ['z', 'x', 'q', 'm', 'a', 'n', 'g', 'o', 's', 't', 'e', 'e', 'n']))
# # print(isWordGuessed(secretWord, lettersGuessed))
# #False