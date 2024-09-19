def custom_write(file_name, strings):

    file = open(file_name, 'w', encoding='utf-8')

    strings_positions = {}

    for i, line in enumerate(strings):
        pos = file.tell()
        file.write(line + '\n')
        strings_positions[i + 1, pos] = line

    file.close()

    return strings_positions




info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
