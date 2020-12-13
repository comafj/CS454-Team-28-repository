# This function finds possible way vector from RGB space
# Suppose that RGB space as 3 dimensional space which each axis are R, G, B from 0 to 255
# Then we can use vector representation to indicate some movements
# It gets 'length' as a input which indicates manhattan distance in 3D dimension
# and return possible vector representation
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


# This function is the simplest version of possible_way
# It does not use any input, but return all possible way which each movements are in range from -1 to 1
def possible_way2():
    ret = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                ret.append([i, j, k])
    return ret


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
# Finding method of n_search closest points
# from c_dict which indicates single RGB space point
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


# Helper function for finding method by search LARGE and small range in turn
# cdict means single RGB space point
# size means how far the movements will go
def large_step(cdict, size):
    dict_set = []
    base_vectors = possible_way2()
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


# Helper function for finding method by search large and SMALL range in turn
# cdict means single RGB space point
# base means how far it is going to base it on
# size means how far the movements will go
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
