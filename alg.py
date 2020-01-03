def sort(scroll, canon):
    list_result = []
    for i in scroll:
        while i == canon[0]:
            list_result.append(canon[0])
            print(list_result)
            break
        while i == canon[1]:
            list_result.append(canon[1])
            print(list_result)
            break
        while i == canon[2]:
            list_result.append(canon[2])
            print(list_result)
            break
    return list_result


inbox_data = list('ССЗСКЗЗЗККСЗССКЗ')
rule = list('ЗСК')
print(sort(inbox_data, rule))
