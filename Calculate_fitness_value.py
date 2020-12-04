import Color_elem_extraction
from Color_elem_extraction import color_element_from_url
import colorsys
from collections import defaultdict


def get_luminance(r, g, b):
    return 0.2126*r + 0.7152*g + 0.0722*b

def calculate_fitness_value(color_elem_list):
    fitness_value_list = [dict() for i in range(len(color_elem_list))]

    color_set = defaultdict(int)

    for index, color_elem in enumerate(color_elem_list):
        foreground_rgba = color_elem[2]
        background_rgba = color_elem[4]

        # Calculate contrast ratio (High is better)
        # https://medium.muz.li/the-science-of-color-contrast-an-expert-designers-guide-33e84c41d156
        foreground_luminance = get_luminance(foreground_rgba.red/256, foreground_rgba.green/256, foreground_rgba.blue/256)
        background_luminance = get_luminance(background_rgba.red/256, background_rgba.green/256, background_rgba.blue/256)
        l1 = max(foreground_luminance, background_luminance)
        l2 = min(foreground_luminance, background_luminance)
        contrast_ratio = (l1 + 0.05) / (l2 + 0.05)
        fitness_value_list[index]['contrast_ratio'] = contrast_ratio


        # Calculate lightness and saturation of background color (Low is better)
        # https://uxmovement.com/content/why-you-should-avoid-bright-saturated-background-colors/
        _, background_lightness, background_saturation = \
            colorsys.rgb_to_hls(background_rgba.red/256, background_rgba.green/256, background_rgba.blue/256)
        fitness_value_list[index]['background_lightness'] = background_lightness
        fitness_value_list[index]['background_saturation'] = background_saturation

        # Calculate the satisfaction of 6:3:1 rule
        # https://medium.com/iconscout/colors-in-ui-design-theory-psychology-practice-f6d6a5e6e04d
        # TODO: caluclate area of each element (It is not completed!)
        foreground_area = color_elem[1].size['height'] * color_elem[1].size['width']
        background_area = color_elem[1].size['height'] * color_elem[1].size['width']
        color_set[(foreground_rgba.red/256, foreground_rgba.blue/256, foreground_rgba.green/256)] = foreground_area
        color_set[(background_rgba.red/256, background_rgba.blue/256, background_rgba.green/256)] = background_area

        fitness_value = (min(contrast_ratio, 4.5) / 4.5) ** 2 * 2 + \
                        (1 - background_saturation) / 0.8 + \
                        (1 - background_lightness) / 0.8

        fitness_value_list[index]['fitness_value'] = fitness_value

    # calculate the number of colors used in UI (Low is better, about 5 is best case)
    number_of_colors = len(color_set)

    # TODO: how to define fitness value?
    #print(number_of_colors)
    #print(color_set)

    return fitness_value_list

if __name__ == "__main__":
    test_url = "https://sattamatkamarket.in/"
    a = color_element_from_url(test_url)
    b = calculate_fitness_value(a)
    print(b)