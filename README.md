# CS454-Team-28-repository
This repository is for the team project of 2020 Fall CS454 "AI Based Software Engineering". Team member are Deokhwa Kim, Minseon Hwang, and Beomsik Park. Our project topic is "Automated improvement of Browser Layout using Search-based Techniques". We referred to the paper "Automated repair of layout cross browser issues using search-based techniques", this paper has referred layout Cross Browser Issue(XBI). We thought that color is also important feature of webpages so we will implement automatic tool to improve webpage's color distribution.

## Project objectives
- Enter a strange web page and improve its color
- Set colors so that the site feels similar to the user

## Color_elem_extraction.py
This is file for extraction from the URL. Function "color_element_from_URL" gets URL as input and returns list of elements information.
Each piece of information consists of this: [index, text element, text element's color, background element, background element's color].
