line = input()
brackets = []
error = 0

for i in line:
    if i == '(':
        brackets.append(i)
    elif i == ')':
        if len(brackets) != 0:
            brackets.pop()
        elif len(brackets) == 0:
            error = -1

if len(brackets) != 0:
    error = -1
if error != 0:
    print('ERROR')
else:
    print('OK')

