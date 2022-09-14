smaller = []
larger = []
sorted_list = []
unsorted_list = [5,9,1,7,6,2,0]

def sort(unsorted_list):
    p = unsorted_list[5]
    for element in range(len(unsorted_list)):
        if unsorted_list[element] < p:
            smaller.append(unsorted_list[element])
        elif unsorted_list[element] > p:
           larger.append(unsorted_list[element])
    if len(smaller) > 1:
        smaller.sort()
    if len(larger) > 1:
        larger.sort()
    sorted_list.extend(smaller)
    sorted_list.append(p)
    sorted_list.extend(larger)
    print(sorted_list)
    return sorted_list

sort(unsorted_list)
