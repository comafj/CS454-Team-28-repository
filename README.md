# CS454-Team-28-repository
This repository is for the team project of 2020 Fall CS454 "AI Based Software Engineering". Team member are Deokhwa Kim, Minseon Hwang, and Beomsik Park. Our project topic is "Automated improvement of Browser Layout using Search-based Techniques". We referred to the paper "Automated repair of layout cross browser issues using search-based techniques", this paper has referred layout Cross Browser Issue(XBI). We thought that color is also important feature of webpages so we will implement automatic tool to improve webpage's color distribution.

## Project objectives
- Enter a strange web page and improve its color
- Set colors so that the site feels similar to the user

## Color_elem_extraction.py
This is file for extraction from the URL. Function "color_element_from_URL" gets URL as input and returns list of elements information.
Each piece of information consists of this: [index, text element, text element's color, background element, background element's color].

## Calculate_fitness_value.py
This extract criterions to judge whether color combination is good or not.
Each piece of criterions are [contrast_ratio, background_saturation, background_lightness, golden_rule_satisfaction, number_of_colors]

## Local_search.py
This is file for finding near RGB value set. Start with some RGB value dictionary, find some local neighbours of it.

## evalutation.py
This is file which contains main function. It executes whole pipeline to solve color issues in HTML file, and print the result of evaluation.

## Change_color.py
This file contains a function that changes color. Enter the Web Element as input. Change the font color or background color of the that element.

## Clustering.py
This file contains a function that clusters elements with RGB values. At second search, we wanted to match the golden ratio of the colors that make up the page. The golden ratio is 6:3:1. We created this file to check the ratio.