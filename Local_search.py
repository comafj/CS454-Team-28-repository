import numpy as np
import itertools


# Main Input : cdict from the function of First_search
#              dictionary form of {red: ??, green: ?? blue: ??, alpha: ??}
#              red, green, blue value are from 0 to 255, and alpha is from 0 to 1


def possible_way_bak(length):
    a = np.array([1, 0, 0])
    b = np.array([0, 1, 0])
    c = np.array([0, 0, 1])
    closest = [a, b, c]
    if length == 1:
        closest = [i.tolist() for i in closest]
        return closest
    else:
        result = []
        for i in possible_way(length - 1):
            for j in closest:
                result.append((i + j).tolist())
        result.sort()
        result = list(result for result, _ in itertools.groupby(result))
        return result


def possible_way(length):
    result=[]
    for i in range(length+1):
        secon = range(length-i+1)
        for j in secon:
            k = length - i - j
            empty = [i, j, k]
            result.append(empty)
    return result



def minus_list(list):
    new_list = []
    for i in list:
        new_list.append((np.multiply(-1, i)).tolist())
    return new_list


def final_ways(length):
    plus_way = possible_way(length)
    minus_way = minus_list(plus_way)
    return plus_way+minus_way


def find_local_values(cdict, length):
    dict_set = []
    candidate_list = final_ways(length)
    for cl in candidate_list:
        red_add = cl[0]
        green_add = cl[1]
        blue_add = cl[2]
        if (cdict['red'] + red_add)<0 or (cdict['red'] + red_add)>255 or (cdict['green'] + green_add)<0 or (cdict['green'] + green_add)>255 or (cdict['blue'] + blue_add)<0 or (cdict['blue'] + blue_add)>255:
            continue
        new_dict = {'red': cdict['red'] + red_add, 'green': cdict['green'] + green_add,
                    'blue': cdict['blue'] + blue_add, 'alpha': cdict['alpha']}
        dict_set.append(new_dict)
    return dict_set



#tdict = {'red': 0, 'green': 0, 'blue': 0, 'alpha': 1}
#elem_length = 1
#print(final_ways(elem_length))
#print(find_local_values(tdict, elem_length))