def sort(scroll, canon):
    first = []
    second = []
    third = []
    for i in scroll:
        if i == canon[0]:
            first.append(canon[0])
    for i in scroll:
        if i == canon[1]:
            second.append(canon[1])
    for i in scroll:
        if i == canon[2]:
            third.append(canon[2])
    list_result = first + second + third
    return list_result


inbox_data = list('ССЗСКЗЗЗККСЗССКЗ')
rule = list('СКЗ')
print(sort(inbox_data, rule))
