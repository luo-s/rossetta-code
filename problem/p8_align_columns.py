# # Given an array of many lines, where fields within a line are delineated by a single $ character, write a program that aligns each column of fields by ensuring that words in each column are separated by at least one space. Further, allow for each word in a column to be either left justified, right justified, or center justified within its column.

# Note that:
# The example input texts lines may, or may not, have trailing dollar characters.
# All columns should share the same alignment.
# Consecutive space characters produced adjacent to the end of lines are insignificant for the purposes of the task.
# Output text will be viewed in a mono-spaced font on a plain text editor or basic terminal. Lines in it should be joined using new line character (\n).
# The minimum space between columns should be computed from the text and not hard-coded.
# It is not a requirement to add separating characters between or around columns.
# For example, one of the lines from the testText, after justifying to the right, left and center respectively:

# https://www.geeksforgeeks.org/python/string-alignment-in-python-f-string/

from itertools import zip_longest
def formatText(input, justification):
    # breakdown the testText into a list of rows, each row a list of words.
    parts = [line.rstrip("$").split("$") for line in testText]
    
    # zip_longest transpose rows to columns, padding with empty string ''
    # widths[i] is the max word length of ith col
    widths = [max(len(word) for word in col) for col in zip_longest(*parts, fillvalue='')]
    
    # loop justify through ["<_Left", "^_Center", ">_Right"]
    for justify in "<_Left ^_Center >_Right".split():
        # destructuring
        j, jtext = justify.split('_')
        
        if justification == jtext.lower():
            # print title
            print(f"{jtext} column-aligned output:\n")
            
            # print aligned text using F-string format specifiers, line by line
            for line in parts:
                print(' '.join(f"{word:{j}{width}}" for width, word in zip(widths, line)))
            
            # separator line
            print("- " * 52)
            break

testText = [
    'Given$a$text$file$of$many$lines',
    'where$fields$within$a$line$',
    'are$delineated$by$a$single$"dollar"$character',
    'write$a$program',
    'that$aligns$each$column$of$fields$',
    'by$ensuring$that$words$in$each$',
    'column$are$separated$by$at$least$one$space.',
    'Further,$allow$for$each$word$in$a$column$to$be$either$left$',
    'justified,$right$justified',
    'or$center$justified$within$its$column.'
]   

formatText(testText, 'left')
formatText(testText, 'center')
formatText(testText, 'right')