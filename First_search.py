import Color_elem_extraction as Cee
import Calculate_fitness_value as Cfv
from selenium.webdriver.support.color import Color
import Local_search as ls
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#print("First search start")
test_url_1 = "https://sattamatkamarket.in/"
test_url_2 = "https://matkaguru.in/"
test_url_3 = "http://www.valleyisleaquatics.com/"  # Doesn't work well
test_url_4 = "http://www.greatdreams.com"  # All fitness_value is above 4.5
test_url_5 = "https://www.theworldsworstwebsiteever.com/"  # Only 5 elements
fitness_th = 3  # A standard for how bad the user would consider bad


# Convert selenium's color type variable into dictionary type variable
def color_to_cdict(color_rgba):
    cdict = {'red': color_rgba.red, 'green': color_rgba.green, 'blue': color_rgba.blue, 'alpha': color_rgba.alpha}
    return cdict


# Convert dictionary type variable into selenium's color type variable
def cdict_to_color(cdict):
    cstr = f"rgba({cdict['red']}, {cdict['green']}, {cdict['blue']}, {cdict['alpha']})"
    color = Color.from_string(cstr)
    return color


# Using compact_find function of Local_search file, find only nearest points from the given RGB point
def do_compact_search(color_result, fit_dict):
    foreground_rgba = color_result[2]
    background_rgba = color_result[4]

    fdict = color_to_cdict(foreground_rgba)
    bdict = color_to_cdict(background_rgba)

    local_dict_list = ls.compact_find(fdict, 100)
    local_result = []
    for ld in local_dict_list:
        to_color = cdict_to_color(ld)
        new_single_r = color_result
        new_single_r[2] = to_color
        local_result.append(new_single_r)

    lfit_list = Cfv.calculate_fitness_value(local_result)
    max_result = [fit_dict['fitness_value'], foreground_rgba]

    for lr, lfl in zip(local_result, lfit_list):
        if lfl['fitness_value'] > max_result[0]:
            max_result[0] = lfl['fitness_value']
            max_result[1] = lr[2]
    return max_result


# Finding method by searching large range and small range in turn
# from the single RGB space point
def do_step_search(color_result, fit_dict):
    foreground_rgba = color_result[2]
    print(foreground_rgba)
    background_rgba = color_result[4]
    fdict = color_to_cdict(foreground_rgba)

    wall_around = ls.large_step(fdict, 1) + ls.large_step(fdict, 10) + ls.large_step(fdict, 50) + \
                  ls.large_step(fdict, 100)

    wall_result = []
    wfit_list = []
    for wa in wall_around:
        to_color = cdict_to_color(wa)
        new_single_r = color_result  # Because it is shallow copy, all new_single_r are same instances.
        new_single_r[2] = to_color
        # wall_result.append(new_single_r)
        wall_result.append(to_color)
        wfit_list += Cfv.calculate_fitness_value([new_single_r])

    # print(wfit_list)
    max_result = [fit_dict['fitness_value'], foreground_rgba]

    better_points = []
    max_fitness = 0
    max_fitness_color = None
    for wr, wfl in zip(wall_result, wfit_list):
        if wfl['fitness_value'] > fit_dict['fitness_value']:
            # bp = wr[2]
            bp = wr
            better_points.append(bp)
            if wfl['fitness_value'] > max_fitness:
                max_fitness = wfl['fitness_value']
                max_fitness_color = bp
                # print(max_fitness, max_fitness_color)

    # if len(better_points) > 0:
        # print improved fitness
        # print("NO RANDOM")
        # print(f"current fitness value = {fit_dict['fitness_value']}")
        # print(f"improved fitness value = {max_fitness}")
        # print(f"Then foreground color will be {max_fitness_color}")
        # print(f"And, background color will be {background_rgba}")

    if len(better_points) == 0:
        # print("It's RANDOM")
        copy_list = wall_result
        random.shuffle(copy_list)
        for i in range(5):
            better_points.append(copy_list[i])

    # print(len(better_points))
    bp_dict = [color_to_cdict(bp) for bp in better_points]
    adj_points = []
    for bd in bp_dict:
        adj_points += ls.small_step(bd, 2, 1) + ls.small_step(bd, 4, 1)
    a_result = []
    afit_list = []

    for ap in adj_points:
        to_color = cdict_to_color(ap)
        new_single_r = color_result  # Because it is shallow copy, all new_single_r are same instances.
        new_single_r[2] = to_color
        # wall_result.append(new_single_r)
        a_result.append(to_color)
        afit_list += Cfv.calculate_fitness_value([new_single_r])

    last_points = []
    max_max_fitness = 0
    max_max_fitness_color = None
    for ar, afl in zip(a_result, afit_list):
        if afl['fitness_value'] > fit_dict['fitness_value']:
            # bp = wr[2]
            bp = ar
            last_points.append(bp)
            if afl['fitness_value'] > max_max_fitness:
                max_max_fitness = afl['fitness_value']
                max_max_fitness_color = bp
                # print(max_max_fitness, max_max_fitness_color)

    if len(last_points) > 0:
        # print("LAST RESULT")
        print(f"current fitness value = {fit_dict['fitness_value']}")
        print(f"improved fitness value = {max_max_fitness}")
        print(f"Then foreground color will be {max_max_fitness_color}")
        print(f"And, background color will be {background_rgba}")

    return max_max_fitness_color, max_max_fitness


if __name__ == "__main__":
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(test_url_1)

    Cee_result = Cee.color_element_from_url(browser, test_url_1)
    # print(len(Cee_result))
    fit_dict_list = Cfv.calculate_fitness_value(Cee_result)
    # print(len(fit_dict_list))
    # for cr, fdl in zip(Cee_result, fit_dict_list):
    #    # print(fdl['fitness_value'])
    #    if fdl['fitness_value'] < fitness_th:
    #        print("DOING LOCAL SEARCH...")
    #        dls = do_compact_search(cr, fdl)
    #        print(dls[0] - fdl['fitness_value'])

    for cr, fdl in zip(Cee_result, fit_dict_list):
        if fdl['fitness_value'] < fitness_th:
            print("DOING STEP SEARCH...")
            dss = do_step_search(cr, fdl)
