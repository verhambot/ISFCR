from flag import flag

output_flag = ''

for index, character in enumerate(flag):
  if index % 2 == 0:
    output_flag += chr(ord(character) + 1)
  else:
    output_flag += chr(ord(character) - 1)

with open('output.txt', 'w') as file:
  file.write(output_flag)
