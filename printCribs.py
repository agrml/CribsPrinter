#! /usr/bin/python3

"""
Script helps you to print a stack of cribs. Read more bellow in Russian.

---
Предполагается, что у Вас есть учебник из n страниц и Вы хотите распечатать его по m^2 страниц на сторону A4 (т.е. по m страниц в ряд и m таких рядов на сторону A4).
Вы вводите:
 - желаемое число страниц учебника на однин раяд в конечном A4;
 - число страниц в учебнике.
Вы получаете список номеров страниц, который нужно вставить в поле "Page numbers" окна печати. Также в окне печати вы выбираете печать по m на m страниц документа на страниуцу A4.
Напечатав документ, Вам остается разрезать A4 на стопки и сложить их друг поверх друга, начиная с правой нижней. Двигаясь налево (до упора), а затем вверх.
PROFIT!
"""

import math
import copy

n = int(input("Pages per row: "))
numPages = int(input("Pages in the document: "))

numStacks = n ** 2
numPagesPerStack = math.ceil(numPages / numStacks)

stacks = []
pageNumber = 0
# form stacks
for stackNumber in range(numStacks):
    stack = []
    while True:
        # numPages marks "white pages" in the last stacks
        stack.append(pageNumber + 1 if pageNumber < numPages else numPages)
        pageNumber += 1
        if not(pageNumber % numPagesPerStack):
            break
    stacks.append(copy.copy(stack))

# form papers
papers = []
for i in range(len(stacks[0])):
    paper = []
    for j in range(numStacks):
        paper.append(stacks[j][i])
    papers.append(copy.copy(paper))

s = ""
for paper in papers:
    for number in paper:
        s += str(number) + ", "
print(s[:-2])
