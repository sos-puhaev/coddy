def sort_list(list_1, list_2):
    list = []
    res = []
    list = list_1 + list_2
    for item in list:
        for i in range(len(res)):
            if item > res[i]:
                res.insert(i, item)
                break
        else:
            res.append(item)
    return res

list1 = [1, 3, 7, 9, 11]
list2 = [2, 4, 6, 8, 10]

print(sort_list(list1, list2))
