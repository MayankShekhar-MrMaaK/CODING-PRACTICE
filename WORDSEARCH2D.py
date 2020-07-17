# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 23:17:39 2020

@author: MrMaak
"""
# WORD SEARCH

# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
 

# Constraints:

# board and word consists only of lowercase and uppercase English letters.
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
# Accepted



def searchword(board, word, i):
    for i in range (0, len(board)):
        for j in range( 0, len(board[i])):
            if board[i][j]== word[0] and dfs(board, word, i, j, 0):
                return True
    return False

def dfs(board, word, i, j, count):
    if count==len(word):
        return True
    if i<0 or i>=len(board) or j<0 or j>= len(board[i]) or board[i][j]!= word[count]:
        return False
    temp= board[i][j]
    board[i][j]=""
    found= dfs(board, word, i-1, j, count+1) or dfs(board, word, i+1, j, count+1)or dfs(board, word, i, j-1, count+1) or dfs(board, word, i, j+1, count+1)
    board[i][j]=temp
    return found
    
board =[
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']]
word="SEE"
print(searchword(board, word, 0))