"""Justifying Text with the rjust(), ljust(), and center() Methods
The rjust() and ljust() string methods return a padded version of the string they are called on, with spaces inserted to justify the text. The first argument to both methods is an integer length for the justified string. Enter the following into the interactive shell:
>>> 'Hello'.rjust(10)
'     Hello'
>>> 'Hello'.rjust(20)
'              Hello'
>>> 'Hello, World'.rjust(20)
'         Hello, World'
>>> 'Hello'.ljust(10)
'Hello     '

'Hello'.rjust(10) says that we want to right-justify 'Hello' in a string of total length 10. 'Hello' is five characters, so five spaces will be added to its left, giving us a string of 10 characters with 'Hello' justified right.
An optional second argument to rjust() and ljust() will specify a fill character other than a space character. Enter the following into the interactive shell:
>>> 'Hello'.rjust(20, '*')
'***************Hello'
>>> 'Hello'.ljust(20, '-')
'Hello---------------'"""

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
for i in range(0,3):
    for j in range(0,3):
        print(tableData[j][i].ljust(10),end="")
    print()