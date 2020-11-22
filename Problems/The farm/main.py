money = int(input())
# money = 650
animals = [
    ['sheep', 6769], ['cow', 3848], ['pig', 1296], ['goat', 678], ['chicken', 23]
]

if money < 23:
    print('None')

for i in range(len(animals)):
    qty = money // animals[i][1]
    if 0 < qty < 2:
        print(f'{round(qty)} {animals[i][0]}')
        break
    elif qty >= 2:
        if animals[i][0] == 'sheep':
            print(f'{round(qty)} {animals[i][0]}')
        else:
            print(f'{round(qty)} {animals[i][0]}s')
        break