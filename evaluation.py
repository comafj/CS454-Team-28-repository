# evaluation.py
# It executes first_search, and change the color of text in web page.

import Color_elem_extraction as Cee
import Calculate_fitness_value as Cfv
from selenium.webdriver.support.color import Color
import Local_search as ls
import random
import First_search
import change_color
import Second_search
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

test_url_1 = "https://sattamatkamarket.in/"
test_url_2 = "https://matkaguru.in/"
test_url_3 = "http://www.valleyisleaquatics.com/"  # Doesn't work well
test_url_4 = "http://www.greatdreams.com"  # All fitness_value is above 4.5
test_url_5 = "https://www.theworldsworstwebsiteever.com/"  # Only 5 elements
fitness_th = 3 # A standard for how bad the user would consider bad

if __name__ == "__main__":
    start_time = time.time()

    browser = webdriver.Chrome(ChromeDriverManager().install())
    # Project repository, it can be different
    # browser.get("C:/CS454-Team-28-repository/worst_web_page_example.html")
    browser.get("C:/CS454-Team-28-repository/example_4.html")
    # get color elements from url
    Cee_result = Cee.color_element_from_url(browser)

    # calculate fitness values of color elements.
    fit_dict_list = Cfv.calculate_fitness_value(Cee_result)

    total_issues = 0
    solved_issues = 0
    improve_ratio = 1.2
    inter_result = []
    # Identifier decides whether to change text or background.
    # 't' for text, 'b' for background
    identifier = 't'

    # For each elements, search new color which can improve fitness value.
    for i, (cr, fdl) in enumerate(zip(Cee_result, fit_dict_list)):
        if fdl['fitness_value'] < fitness_th:
            total_issues += 1

            # Search new color.
            print("DOING STEP SEARCH...")
            text_change_color, text_imp_fitness = First_search.do_step_search(cr, fdl, 't')
            back_change_color, back_imp_fitness = First_search.do_step_search(cr, fdl, 'b')
            # Continue if there is no chance of improvement in both colors
            if (text_change_color == None) and (back_change_color == None):
                continue

            # Count it if it solves the color problem.
            if text_imp_fitness + fdl['fitness_value'] > improve_ratio * fdl['fitness_value']:
                solved_issues += 1

            # Change the color of elements to solve color problem.
            if text_change_color != None:
                text_to_color = change_color.color_to_format(text_change_color)
                inter_result.append([Cee_result[i][1], change_color.color_to_format(Cee_result[i][2]), \
                                     text_to_color, text_imp_fitness, "t"])
            if back_change_color != None:
                back_to_color = change_color.color_to_format(back_change_color)
                inter_result.append([Cee_result[i][3], change_color.color_to_format(Cee_result[i][4]), \
                                     back_to_color, back_imp_fitness, "b"])

    # print(f"Solved {solved_issues}/{total_issues} issues.")
    # print(inter_result)
    Second_search.combi_search(browser, inter_result)
    end_time = time.time()
    print(f"Total {end_time-start_time:.1f} s elapsed.")
