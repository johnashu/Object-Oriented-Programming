
#create the matrix
num_order = [15, 14, 1, 6, 9, 11, 4, 12, 0, 10, 7, 3, 13, 8, 5, 2]
matrix = [num_order[i:i +4] for i in range(0, len(num_order), 4)]

for i in matrix:
    print(i)

# rrrulddluuuldrurdddrullulurrrddldluurddlulurruldrdrd

#starting indexes
for i in num_order:
    if i == 1:
        num1 = i
for i in num_order:
    if i == 2:
        num2 = i
for i in num_order:
    if i == 3:
        num3 = i        
for i in num_order:
    if i == 4:
        num4 = i
for i in num_order:
    if i == 5:
        num5 = i
for i in num_order:
    if i == 6:
        num6 = i
for i in num_order:
    if i == 7:
        num7 = i        
for i in num_order:
    if i == 8:
        num8 = i
for i in num_order:
    if i == 9:
        num9 = i
for i in num_order:
    if i == 10:
        num10 = i
for i in num_order:
    if i == 11:
        num11 = i        
for i in num_order:
    if i == 12:
        num12 = i
for i in num_order:
    if i == 13:
        num13 = i
for i in num_order:
    if i == 14:
        num14 = i
for i in num_order:
    if i == 15:
        num15 = i        
for i in num_order:
    if i == 0:
        num16 = i                        
        
print(num_order.index(num1))
print(num_order.index(num2))
print(num_order.index(num3))
print(num_order.index(num4))
print(num_order.index(num5))
print(num_order.index(num6))
print(num_order.index(num7))
print(num_order.index(num8))
print(num_order.index(num9))
print(num_order.index(num10))
print(num_order.index(num11))
print(num_order.index(num12))
print(num_order.index(num13))
print(num_order.index(num14))
print(num_order.index(num15))
print(num_order.index(num16))

positions = {'pos1': matrix[0][0],
'pos2': matrix[0][1],
'pos3': matrix[0][2],
'pos4': matrix[0][3],
'pos5': matrix[1][0],
'pos6': matrix[1][1],
'pos7': matrix[1][2],
'pos8': matrix[1][3],
'pos9': matrix[2][0],
'pos10': matrix[2][1],
'pos11': matrix[2][2],
'pos12': matrix[2][3],
'pos13': matrix[3][0],
'pos14': matrix[3][1],
'pos15': matrix[3][2],
'pos16': matrix[3][3]
}


print(positions)    #[:4], '\n', positions[4:9], '\n', positions[8:13], '\n', positions[12:])

