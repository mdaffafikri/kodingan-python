import math

height = int(input('Type NUMBER of height : '))

# pyramid = ['*','*','*','*','*','*','*']

pyramid = []
for i in range(height):
    pyramid.append('·')


median = math.ceil(len(pyramid)/2-1)

print(median)

for i in range(median+1):
    if i == 0:
        pyramid[median] = '*'
        print(''.join(pyramid))

    else:
        pyramid[median-i] = '*'
        pyramid[median+i] = '*'
        print(''.join(pyramid))