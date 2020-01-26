#Print the languages that are inferior to Python

py = {'Python': 'Rocks', 'inferior': ['java', 'cobol']}
n = 'inferior'
for i in py:
    if n in i:
        print(py[i])