import Calculate_fitness_value as Cfv
import Color_elem_extraction as Cee
import change_color as cc
import Clustering as Clust


def color_to_tuple(color):
    result_tuple = (color.red, color.green, color.blue)
    return result_tuple


def gold_ratio(browser):
    cee_result = Cee.color_element_from_url(browser)
    cl_list = []
    color_size_dict = {}
    for ce in cee_result:
        text_size_dict = ce[1].size
        cl_list.append(color_to_tuple(ce[2]))
        text_area = text_size_dict['height'] * text_size_dict['width']
        color_size_dict[color_to_tuple(ce[2])] = text_area
        back_size_dict = ce[3].size
        cl_list.append(color_to_tuple(ce[4]))
        back_area = back_size_dict['height'] * back_size_dict['width']
        color_size_dict[color_to_tuple(ce[4])] = back_area
    clust_result = Clust.Clustering(cl_list, 3)
    color_ratio = []
    for cr in clust_result:
        size_sum = 0
        for t in cr:
            size_sum += color_size_dict[t]
        color_ratio.append(size_sum)
    color_ratio.sort(reverse=True)
    # print(color_ratio)
    b_ratio = color_ratio[0] / color_ratio[2]
    s_ratio = color_ratio[1] / color_ratio[2]
    golden = (b_ratio - 6) / 9 + (s_ratio - 3) / 9
    return 1-abs(golden)


def calc_fit(browser):
    cee_result = Cee.color_element_from_url(browser)
    fit_dict_list = Cfv.calculate_fitness_value(cee_result)
    page_fit = 0
    for fd in fit_dict_list:
        page_fit += fd['fitness_value']
    return page_fit


def combi_search(browser, inter_result):
    print("DOING COMBI SEARCH...")
    ifv = calc_fit(browser) + gold_ratio(browser)
    print(f"Initial fitness value is {ifv}.")
    total_changes = len(inter_result)
    applied_changes = 0
    inter_result.sort(key=lambda x: x[3], reverse=True)
    current_iter = inter_result
    next_iter = []
    while True:
        for ir in current_iter:
            before_fit = calc_fit(browser) + gold_ratio(browser)
            cc.change_color(browser, ir[0], ir[2], ir[4])
            after_fit = calc_fit(browser) + gold_ratio(browser)
            if after_fit < before_fit:
                cc.change_color(browser, ir[0], ir[1], ir[4])
                next_iter.append(ir)
                continue
                # break
            else:
                applied_changes += 1
        if len(current_iter) == len(next_iter):
            break
        else:
            current_iter = next_iter
            next_iter = []
    print(f"Applied {applied_changes}/{total_changes} changes.")
    ffv = calc_fit(browser) + gold_ratio(browser)
    print(f"Final fitness value is {ffv}.")
