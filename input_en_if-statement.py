# if statement

getal_1 = input('Noem je eerste getal. ')
getal_2 = input('Noem je tweede getal. ')

if getal_1 > getal_2:
    max = getal_1
    print('a is het grootste getal: ' + str(max))

elif getal_1 < getal_2:
    min = getal_1
    print('a is het kleinste getal: ' + str(min))

else:
    print('a en b zijn even groot')

print('Het minimum is: ' + str(min))
print('Het maximum is: ' + str(max))