import Color_elem_extraction
from Color_elem_extraction import color_element_from_url
import colorsys
from collections import defaultdict
import numpy as np
import cv2

def linear_to_srgb(c):
    if c <= 0.0404482362771082:
        return c/12.92
    else:
        return ((c+0.055)/1.055)**2.4

def get_luminance(r, g, b):
    r, g, b = linear_to_srgb(r), linear_to_srgb(g), linear_to_srgb(b)
    return 0.2126*r + 0.7152*g + 0.0722*b

def fitness_value(f_color, b_color):
    f_r, f_g, f_b = f_color
    b_r, b_g, b_b = b_color
    f_r, f_g, f_b, b_r, b_g, b_b = f_r/255, f_g/255, f_b/255, b_r/255, b_g/255, b_b/255
    f_luminance = get_luminance(f_r, f_g, f_b)
    b_luminance = get_luminance(b_r, b_g, b_b)

    l1 = max(f_luminance, b_luminance)
    l2 = min(f_luminance, b_luminance)

    print(l1, l2)

    constrast_ratio = (l1 + 0.05) / (l2 + 0.05)
    max_contrast_ratio = max((1 + 0.05) / (b_luminance + 0.05), (b_luminance + 0.05) / (0.05))
    print(max_contrast_ratio)

    _, background_lightness, background_saturation = colorsys.rgb_to_hls(b_r, b_g, b_b)

    print(constrast_ratio, background_lightness, background_saturation)

    # Give high weight for contrast ratio
    # Set 4.5 as a minimal criteria for contrast ratio
    # Take square for contrast_ratio because low contrast ratio is terrible
    # fitness_value = (min(constrast_ratio, 4.5) / 4.5) ** 2 * 2 + \
    #                 (1 - background_saturation) + \
    #                 (1 - background_lightness)
    fitness_value = (constrast_ratio / max_contrast_ratio) * 2 + \
                    (1 - background_saturation) + \
                    (1 - background_lightness)

    return constrast_ratio, background_lightness, background_saturation, fitness_value

if __name__ == "__main__":
    f_color = (0, 0, 0)
    b_color = (255, 255, 255)

    fonts = cv2.FONT_HERSHEY_SIMPLEX

    img = np.zeros((400, 600, 3), np.uint8)

    c, bl, bs, f = fitness_value(f_color, b_color)

    img[:] = tuple(reversed(b_color))

    text =  f"f={f:.3f} SAMPLE"

    # get boundary of this text
    textsize = cv2.getTextSize(text, fonts, 0.7, 2)[0]

    # get coords based on boundary
    textX = (img.shape[1] - textsize[0]) / 2
    textY = (img.shape[0] + textsize[1]) / 2

    cv2.putText(img, text, (int(textX), int(textY)), fonts, 0.7, tuple(reversed(f_color)), 2, cv2.LINE_AA)

    cv2.imshow('sample', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()