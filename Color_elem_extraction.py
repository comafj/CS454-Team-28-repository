from selenium import webdriver
from selenium.webdriver.support.color import Color
from webdriver_manager.chrome import ChromeDriverManager
#import time
#from collections import Counter

def color_element_from_URL(url):
    # browser = webdriver.Chrome()
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)

    candi_elems = browser.find_elements_by_xpath("//*[contains (@ style, 'color')]")
    result = []

    index = 1
    for ce in candi_elems:
        single_r = [] # single_r 형식 : [index, text element, text color, background element, background color]
        single_r.append(index)
        
        p_of_ce = ce.find_element_by_xpath("..")
        if ce.text == "":
            continue
        style_of_ce = ce.get_attribute("style")
        p_back = p_of_ce.value_of_css_property("background-color") 
        for soc in style_of_ce.split(";"):
            if "color" in soc:
                cstr = soc.split(":")[1].strip()
                ccol = Color.from_string(cstr) # 글자 색깔을 Color class로 표현
                single_r.append(ce)
                single_r.append(ccol)
                break
        p_back = Color.from_string(p_back) # 배경 색깔을 Color class로 표현
        single_r.append(p_of_ce)
        single_r.append(p_back)
        index+=1
        result.append(single_r)
    return result

if __name__ == "__main__":
    test_url = "https://sattamatkamarket.in/"
    print(color_element_from_URL(test_url))