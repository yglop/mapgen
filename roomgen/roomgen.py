
data = None
room = list()


with open('./text.txt', 'r') as text:
    data = text.readlines()

for line in data:
    _line = [i for i in line.strip('\n')]
    room.append(_line)

with open('./room.txt', 'w') as text:
    print('    [', file=text)
    for i in room:
        print(f'        {i},', file=text)
    print('    ],', file=text)

for i in room:
    print(i)



