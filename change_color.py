#The Web Element Type object is entered.
def change_color(browser, elem, color, cf):
    #Change the browser after deciding whether to change the background or color of the writing.
    if cf == 'b':
        browser.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", elem, "style", elem.get_attribute("style")+"background-color:"+color)
    elif cf == 't':
        browser.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", elem, "style", elem.get_attribute("style")+"color:"+color)
    

def color_to_format(sup_color):
    red = ('0x%0.2X' % sup_color.red)[2:]
    green = ('0x%0.2X' % sup_color.green)[2:]
    blue = ('0x%0.2X' % sup_color.blue)[2:]
    sup_to_color = f"#{red}{green}{blue}"
    return sup_to_color
