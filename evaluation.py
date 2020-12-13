# evaluation.py
# It executes first_search, and change the color of text in web page.

import Color_elem_extraction as Cee
import Calculate_fitness_value as Cfv
from selenium.webdriver.support.color import Color
import Local_search as ls
import random
import First_search
import change_color
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

test_url_1 = "https://sattamatkamarket.in/"
test_url_2 = "https://matkaguru.in/"
test_url_3 = "http://www.valleyisleaquatics.com/"  # Doesn't work well
test_url_4 = "http://www.greatdreams.com"  # All fitness_value is above 4.5
test_url_5 = "https://www.theworldsworstwebsiteever.com/"  # Only 5 elements
fitness_th = 3 # A standard for how bad the user would consider bad

if __name__ == "__main__":
    browser = webdriver.Chrome(ChromeDriverManager().install())
    # Project repository, it can be different
    # browser.get("C:/CS454-Team-28-repository/worst_web_page_example.html")
    browser.get("C:/CS454-Team-28-repository/example_4.html")
    # get color elements from url
    Cee_result = Cee.color_element_from_url(browser, test_url_1)
    # print(len(Cee_result))
    # calculate fitness values of color elements.
    fit_dict_list = Cfv.calculate_fitness_value(Cee_result)
    # print(len(fit_dict_list))
    #for cr, fdl in zip(Cee_result, fit_dict_list):
    #    # print(fdl['fitness_value'])
    #    if fdl['fitness_value'] < fitness_th:
    #        print("DOING LOCAL SEARCH...")
    #        dls = do_local_search(cr, fdl)
    #        print(dls[0] - fdl['fitness_value'])

    total_issues = 0
    solved_issues = 0
    improve_ratio = 1.2

    # For each elements, search new color which can improve fitness value.
    for i, (cr, fdl) in enumerate(zip(Cee_result, fit_dict_list)):
        if fdl['fitness_value'] < fitness_th:
            total_issues += 1

            # Search new color.
            print("DOING STEP SEARCH...")
            max_fitness_color, max_fitness = First_search.do_step_search(cr, fdl)

            # Count it if it solves the color problem.
            if max_fitness > improve_ratio * fdl['fitness_value']:
                solved_issues += 1
            red = ('0x%0.2X' % max_fitness_color.red)[2:]
            green = ('0x%0.2X' % max_fitness_color.green)[2:]
            blue = ('0x%0.2X' % max_fitness_color.blue)[2:]
            to_color = f"#{red}{green}{blue}"
            # Change the color of elements to solve color problem.
            change_color.change_color(browser, Cee_result[i][1], to_color, "t")

    print(f"Solved {solved_issues}/{total_issues} issues.")
