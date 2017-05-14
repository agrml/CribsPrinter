#! /usr/bin/python3

"""
Script helps you to print a stack of cribs. Read more in readme.
"""

import math
import copy

n = 3
try:
    n = int(input("Pages per row [<Enter> for 3]: "))
except ValueError:
    pass
firstPageIdx = 0
try:
    firstPageIdx = int(input("First page [<Enter> for 1]: ")) - 1
except ValueError:
    pass
numPages = int(input("Pages in the document: "))

numStacks = n ** 2
numPagesPerStack = math.ceil((numPages - firstPageIdx) / numStacks)

stacks = []
pageNumber = firstPageIdx
# form stacks
for stackNumber in range(numStacks):
    stack = []
    while True:
        # numPages marks "white pages" in the last stacks
        stack.append(pageNumber + 1 if pageNumber < numPages else numPages)
        pageNumber += 1
        if not((pageNumber - firstPageIdx) % numPagesPerStack):
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
