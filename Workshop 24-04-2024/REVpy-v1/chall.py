import string
from flag import flag

assert len(flag) % 2 == 0
assert all(map(lambda x: x in string.ascii_lowercase + '{}_!', flag))

flag = list(map(ord, flag))
output = []

for index in range(0, len(flag), 2):
  output.append(flag[index] * flag[index + 1])

with open('output.txt', 'w') as file:
  file.write(str(output))
