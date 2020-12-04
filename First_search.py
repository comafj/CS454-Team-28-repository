import Color_elem_extraction as Cee
import Calculate_fitness_value as Cfv
import Test_fitness_function as Tff
from selenium.webdriver.support.color import Color

print("First search start")
test_url_1 = "https://sattamatkamarket.in/"
test_url_2 = "https://matkaguru.in/"
test_url_3 = "http://www.valleyisleaquatics.com/"  # Doesn't work well
test_url_4 = "http://www.greatdreams.com"  # All fitness_value is above 4.5
test_url_5 = "https://www.theworldsworstwebsiteever.com/"  # Only 5 elements
fitness_th = 3 # A standard for how bad the user would consider bad


def color_to_cdict(color_rgba):
    cdict = {'red': color_rgba.red, 'green': color_rgba.green, 'blue': color_rgba.blue, 'alpha': color_rgba.alpha}
    return cdict


def cdict_to_color(cdict):
    cstr = f"rgba({cdict['red']}, {cdict['green']}, {cdict['blue']}, {cdict['alpha']})"
    color = Color.from_string(cstr)
    return color


# TODO : We should implement how to perform local search asap
def do_local_search(color_result, fit_dict):
    new_fit_dict = fit_dict
    foreground_rgba = color_result[2]
    background_rgba = color_result[4]
    # print("DOING LOCAL SEARCH...")
    # print(foreground_rgba)
    fdict = color_to_cdict(foreground_rgba)
    # print(fdict)

    # Place where searching process should be implemented
    fdict['red'] = 123
    # Place where searching process should be implemented

    new_rgba = cdict_to_color(fdict)
    # print(new_rgba)
    # print(foreground_rgba)
    # print(background_rgba)


Cee_result = Cee.color_element_from_url(test_url_1)
# print(len(Cee_result))
fit_dict_list = Cfv.calculate_fitness_value(Cee_result)
# print(len(fit_dict_list))
for cr, fdl in zip(Cee_result, fit_dict_list):
    print(fdl['fitness_value'])
    if fdl['fitness_value'] < fitness_th:
        # print(fdl['contrast_ratio'])
        do_local_search(cr, fdl)
