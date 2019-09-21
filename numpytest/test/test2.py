def count_text(text):
    result = []
    if not text:
        result.append(0)
    for index, temp in enumerate(text, 1):
        if temp != ' ':
            result.append(index)
    print(result)


def count_text_new(text):
    if not text:
        yield 0
    for index, temp in enumerate(text, 1):
        if temp != ' ':
            yield index


result = count_text_new('ddfsafs')
for i in result:
    print(i)
