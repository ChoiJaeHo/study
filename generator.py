def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('test data'):
    print(char)

import os
name = os.path.basename('/name/value/test/abc.txt')
print(name)