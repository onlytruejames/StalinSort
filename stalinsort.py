def stalinSort(list):
    base = list[0]
    sortedList = []
    for thing in list:
        if not thing<base:
            base = thing
            sortedList.append(thing)
    return sortedList

list = [
    5,
    4,
    7,
    3,
    8,
    3,
    9,
    4,
    2,
    0,
    4,
    6
]

print(stalinSort(list))