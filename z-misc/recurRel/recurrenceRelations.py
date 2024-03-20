def tee2(n):
    return (2 * 3 ** n) - 5

for i in range(1, 21):
    print(f'{i:3}: {tee2(i):10}')
