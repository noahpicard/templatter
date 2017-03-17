from generate_utils import *

heading_font_list = [
    'Helvetica Neue',
    'Garamond',
    'Abril Fatface',
    'Raleway',
    'Roboto',
    'Open Sans',
    'Roboto Condensed',
    'Montserrat',
    'Ubuntu',
    'Playfair Display',
    'Inconsolata',
    'Indie Flower',
    'Kalam']

content_font_list = [
    'Helvetica Neue',
    'Times New Roman',
    'Verdana',
    'Raleway',
    'Helvetica Neue',
    'Garamond',
    'Abril Fatface',
    'Raleway',
    'Roboto',
    'Open Sans',
    'Roboto Condensed',
    'Montserrat',
    'Ubuntu',
    'Playfair Display',
    'Inconsolata',
    'Indie Flower',
    'Kalam']


def get_font_set():
    heading_font = pick_one(heading_font_list)
    content_font = pick_one(content_font_list)

    return heading_font, content_font