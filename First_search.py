import Color_elem_extraction as Cee
import Calculate_fitness_value as Cfv
import Test_fitness_function as Tff

print("First search start")
test_url_1 = "https://sattamatkamarket.in/"
test_url_2 = "https://matkaguru.in/"
test_url_3 = "http://www.valleyisleaquatics.com/" # Doesn't work well
test_url_4 = "http://www.greatdreams.com" # All fitness_value is above 4.5
test_url_5 = "https://www.theworldsworstwebsiteever.com/" # Only 5 elements

Cee_result = Cee.color_element_from_url(test_url_1)
# print(Cee_result[0])
# short_list = [Cee_result[0]]
fit_dict_list = Cfv.calculate_fitness_value(Cee_result)
for fd in fit_dict_list:
    print(fd)