from selenium import webdriver
from selenium.webdriver.support.color import Color
from webdriver_manager.chrome import ChromeDriverManager

# It is a function to extract colored element in the given URL or some html file
# First 2 lines of the definition make it extract from the URL
# If not it can be used for some html file by setting the browser
def color_element_from_url(browser, url):
    # browser = webdriver.Chrome(ChromeDriverManager().install())
    # browser.get(url)

    # Find elements which contain 'color' in style attribute
    candi_elems = browser.find_elements_by_xpath("//*[contains(@style, 'color') and \
                                                    not (contains(@style, 'background'))]")
    result = []

    index = 1
    for ce in candi_elems:
        # If there is no text, continue to next element
        if ce.text == "":
            continue
        # single_r format : [index, text element, text color, background element, background color]
        single_r = []
        single_r.append(index)

        # Find parent element of candidate element which indicates background
        p_of_ce = ce.find_element_by_xpath("..")
        style_of_ce = ce.get_attribute("style")
        # Get background color from the parent element
        p_back = p_of_ce.value_of_css_property("background-color") 
        for soc in style_of_ce.split(";"):
            if "color" in soc:
                cstr = soc.split(":")[1].strip()
                ccol = Color.from_string(cstr) # Convert text color to Color class
                single_r.append(ce)
                single_r.append(ccol)
                break
        p_back = Color.from_string(p_back) # Convert background color to Color class
        single_r.append(p_of_ce)
        single_r.append(p_back)
        index += 1
        result.append(single_r)
    return result


if __name__ == "__main__":
    test_url = "https://sattamatkamarket.in/"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("C:/CS454-Team-28-repository/example_3.html")
    cee_test = color_element_from_url(browser, test_url)
    # for i in cee_test:
    #    print(i)