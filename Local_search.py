def possible_way(length):
    result = []
    first_range = range(-length, length + 1)
    for i in first_range:
        i_abs = abs(i)
        j_max_abs = length - i_abs
        second_range = range(-j_max_abs, j_max_abs + 1)
        for j in second_range:
            k_fix_abs = length - i_abs - abs(j)
            result.append([i, j, k_fix_abs])
            if k_fix_abs > 0:
                result.append([i, j, -k_fix_abs])
    return result


# Function to check rgb boundary condition
def rgb_boundary(value, delta):
    if (value + delta) < 0 or (value + delta > 255):
        return True
    else:
        return False


# Main Input : cdict from the function of First_search
#              dictionary form of {red: ??, green: ?? blue: ??, alpha: ??}
#              red, green, blue value are from 0 to 255, and alpha is from 0 to 1


# Function compact_find(cdict, n_search):
# cdict가 나타내는 점을 기준으로 manhattan distance가 1인 점들, 2인 점들, ... 차례로 늘려나가며
# 최종적으로는 항상 n_search개의 결과를 출력한다
# 즉 cdict로부터 가장 가까운 n_search개의 점들에 대해 탐색하는 방법
def compact_find(cdict, n_search):
    dict_set = []
    candidate_list = []
    init_length = 1
    while len(candidate_list) < n_search:
        candidate_list += possible_way(init_length)
        init_length += 1
    candidate_list = candidate_list[:n_search]
    red_val = cdict['red']
    green_val = cdict['green']
    blue_val = cdict['blue']
    for cl in candidate_list:
        red_add = cl[0]
        green_add = cl[1]
        blue_add = cl[2]
        if rgb_boundary(red_val, red_add) or rgb_boundary(green_val, green_add) or rgb_boundary(blue_val, blue_add):
            continue
        new_dict = {'red': red_val + red_add, 'green': green_val + green_add,
                    'blue': blue_val + blue_add, 'alpha': cdict['alpha']}
        dict_set.append(new_dict)
    return dict_set

# It makes total 27 directions to search
def possible_way2():
    ret = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                ret.append([i, j, k])
    return ret

# cdict를 중앙으로 하여 큰 범위를 탐색하고 그 결과를 반환 하는 function
# dictionary cdict는 탐색 기준이 되는 rgb 평면 상의 점을 나타낸다
# int base는 cdict를 기준으로 퍼져나갈 때 몇 가지 방향성을 사용할 것인지를 결정한다
# int size는 base에 의한 방향성을 기준으로 몇 배수를 탐색할 것인지 나타낸다
def large_step(cdict, base, size):
    dict_set = []
    # base_vectors = possible_way(base) # Previous version
    base_vectors = possible_way2()      # New version
    sized_vectors = [[size*val for val in bv] for bv in base_vectors]

    red_val = cdict['red']
    green_val = cdict['green']
    blue_val = cdict['blue']

    for sv in sized_vectors:
        red_add = sv[0]
        green_add = sv[1]
        blue_add = sv[2]
        if rgb_boundary(red_val, red_add) or rgb_boundary(green_val, green_add) or rgb_boundary(blue_val, blue_add):
            continue
        new_dict = {'red': red_val + red_add, 'green': green_val + green_add,
                    'blue': blue_val + blue_add, 'alpha': cdict['alpha']}
        dict_set.append(new_dict)
    return dict_set


def small_step(cdict, base, size):
    dict_set = []
    base_vectors = possible_way(base)
    sized_vectors = [[size*val for val in bv] for bv in base_vectors]

    red_val = cdict['red']
    green_val = cdict['green']
    blue_val = cdict['blue']

    for sv in sized_vectors:
        red_add = sv[0]
        green_add = sv[1]
        blue_add = sv[2]
        if rgb_boundary(red_val, red_add) or rgb_boundary(green_val, green_add) or rgb_boundary(blue_val, blue_add):
            continue
        new_dict = {'red': red_val + red_add, 'green': green_val + green_add,
                    'blue': blue_val + blue_add, 'alpha': cdict['alpha']}
        dict_set.append(new_dict)
    return dict_set


tdict = {'red': 100, 'green': 100, 'blue': 100, 'alpha': 1}
elem_length = 2
#print(len(small_step(tdict, 1, 1)))
#print(len(small_step(tdict, 2, 1)))
#print(len(small_step(tdict, 3, 1)))
#print(len(small_step(tdict, 4, 1)))
#print(len(small_step(tdict, 8, 1)))
#print(len(large_step(tdict, 4, 1)))

#print(len(large_step(tdict, elem_length, 2)))
#print(len(large_step(tdict, elem_length, 5)))
#print(len(large_step(tdict, elem_length, 10)))
#print(len(large_step(tdict, 3, 2)))
#one_step = possible_way(elem_length)
#print(len(one_step))
#ttt = compact_find(tdict, 10)
#print(len(ttt), ttt)

#sum = 0
#for i in range(15):
#    temp = possible_way(i+1)
#    sum+=len(temp)
#    print((i+1, len(temp), sum))
