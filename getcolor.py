from random import *
import math
import colorsys
from colutils import get_random_color, make_color_hsl

pattern_list = {
    'complementary': {
        'colors':[[0, 0, 0], [180, 0, 0]]},
    'complementary /w black': {
        'colors':[['STATIC', 0, 0, 10], [0, 0, 0], [180, 0, 0]]},
    'complementary /w white': {
        'colors':[['STATIC', 0, 0, 95], [0, 0, 0], [180, 0, 0]]},
    'split complementary': {
        'colors':[[0, 0, 0], [150, 0, 0], [210, 0, 0]]},
    'analog': {
        'colors':[[330, 0, 0], [0, 0, 0], [30, 0, 0]]},
    'double split': {
        'colors':[[330, 0, 0], [30, 0, 0], [150, 0, 0], [210, 0, 0]]},
    'triadic': {
        'colors':[[0, 0, 0], [120, 0, 0], [240, 0, 0]]},
    'monochrome': {
        'colors':[[0, 0, 0], [0, 0, 25], [0, 0, 50], [0, 0, 75]]},
    '90comp': {
        'colors':[[0, 0, 0], [90, 0, 0]]},
    '90comp /w black': {
        'colors':[['STATIC', 0, 0, 10], [0, 0, 0], [90, 0, 0]]},
    '90comp /w white': {
        'colors':[['STATIC', 0, 0, 95], [0, 0, 0], [90, 0, 0]]},
    '270comp': {
        'colors':[[0, 0, 0], [270, 0, 0]]},
    '270comp /w black': {
        'colors':[['STATIC', 0, 0, 10], [0, 0, 0], [270, 0, 0]]},
    '270comp /w white': {
        'colors':[['STATIC', 0, 0, 95], [0, 0, 0], [270, 0, 0]]}
}

hue_max = 360
sat_max = 100
light_max = 100


def get_random_color(hue_floor=0, hue_ceil=360, sat_floor=0, sat_ceil=100, light_floor=0, light_ceil=100):
    '''
    Generates a random color using hsl values within the given ranges
    '''
    hue = (random() * (hue_ceil - hue_floor)) + hue_floor
    sat = (random() * (sat_ceil - sat_floor)) + sat_floor
    light = (random() * (light_ceil - light_floor)) + light_floor
    return hue, sat, light


def get_color_list():
    '''
    Generates a random color set
    '''
    sat_ceil = 100
    light_ceil = 85

    sat_floor = 20
    light_floor = 20

    hue, sat, light = get_random_color(sat_ceil=sat_ceil,
                                       sat_floor=sat_floor,
                                       light_floor=light_floor,
                                       light_ceil=light_ceil)

    ind = int(random() * len(pattern_list))
    pattern_name = pattern_list.keys()[ind]
    pattern = pattern_list[pattern_name]['colors']

    color_list = []

    for p in pattern:
        if p[0] == 'STATIC':
            color_hue = (p[1]) % hue_max
            color_sat = (p[2]) % sat_max
            color_light = (p[3]) % light_max
        else:
            color_hue = (hue + p[0]) % hue_max
            color_sat = (sat + p[1]) % sat_max
            color_light = (light + p[2]) % light_max

        color_hue   = round(color_hue, 2)
        color_sat   = round(color_sat, 2)
        color_light = round(color_light, 2)

        color_list.append([color_hue, color_sat, color_light])

    return color_list


def get_colors():
    color_list = get_color_list()
    detail_list = []
    for hsl_list in color_list:
        color_hue = hsl_list[0]
        color_sat = hsl_list[1]
        color_light = hsl_list[2]
        
        rgb_list = colorsys.hls_to_rgb(hsl_list[0] / hue_max,
                                       hsl_list[2] / light_max,
                                       hsl_list[1] / sat_max);
        rgb_max = 255
        rgb_list = map(lambda x: int(round(x * rgb_max)), rgb_list)
        hsl_list = [round(hsl_list[0]) % hue_max, round(hsl_list[1]), round(hsl_list[2])]
        rgb_str = '#' + reduce(lambda x, y: str(x) + format(y, '02x'), rgb_list, '')
        rgb_str2 = 'rgb(' + str(rgb_list[0]) + ',' + str(rgb_list[1]) + ',' + str(rgb_list[2]) + ');'
        print rgb_str2


        detail_list.append([make_color_hsl(color_hue, color_sat, color_light),
                           make_color_hsl(round(color_hue), round(color_sat), round(color_light)) +
                           ' | ' + rgb_str2 + ' | ' + rgb_str, hsl_list])
    return detail_list

def get_color_detail(color):
    hsl_list = color
    color_hue = hsl_list[0]
    color_sat = hsl_list[1]
    color_light = hsl_list[2]
        
    rgb_list = colorsys.hls_to_rgb(hsl_list[0] / hue_max, hsl_list[2] / light_max, hsl_list[1] / sat_max);
    rgb_max = 255
    rgb_list = map(lambda x: int(round(x * rgb_max)), rgb_list)
    hsl_list = [round(hsl_list[0]) % hue_max, round(hsl_list[1]), round(hsl_list[2])]
    rgb_str = '#' + reduce(lambda x, y: str(x) + format(y, '02x'), rgb_list, '')
    rgb_str2 = 'rgb(' + str(rgb_list[0]) + ',' + str(rgb_list[1]) + ',' + str(rgb_list[2]) + ');'
    print rgb_str2


    details = [make_color_hsl(color_hue, color_sat, color_light), make_color_hsl(round(color_hue), round(color_sat), round(color_light)) +
                           ' | ' + rgb_str2 + ' | ' + rgb_str]
    return details

def get_layout_details():
    col_obj = get_layout_colors()

    for ct in col_obj:
        if ct == "len":
            continue
        col = col_obj[ct]
        col_obj[ct] = get_color_detail(col) + [col]
    return col_obj

def get_layout_colors():
    color_list = get_color_list()
    l = len(color_list)
    col_obj = {}#{"main":None,"sub1":None, "sub2":None, "accent":None, "text":None, "len":0}
    col_obj["len"] = l
    #b_col, color_list = get_furthest_color(color_list, 1)

    t_col = get_text_color(get_blend_color(color_list[1:3]))#get_contrast_color(f_col, 2, 50, 50)

    
    if (l == 2):
        col_obj["main"] = color_list[0]
        col_obj["sub1"] = color_list[1]
        col_obj["text"] = t_col
    elif (l == 3):
        col_obj["main"] = color_list[0]
        col_obj["sub2"] = color_list[2]
        col_obj["sub1"] = color_list[1]
        col_obj["text"] = t_col
    elif (l == 4):
        col_obj["main"] = color_list[0]
        col_obj["sub2"] = color_list[2]
        col_obj["accent"] = color_list[3]
        col_obj["sub1"] = color_list[1]
        col_obj["text"] = t_col
    
    return col_obj


def get_contrast_color(col, att, mid, dist):
    ncol = col[:]
    if ncol[att] > mid:
        dist *= -1
    ncol[att] += dist
    return ncol

def get_blend_color(color_list):
    l = float(len(color_list))
    hue = sum(zip(*color_list)[0])/l
    sat = sum(zip(*color_list)[1])/l
    light = sum(zip(*color_list)[2])/l

    col = [hue, sat, light]
    return col


def get_text_color(col):
    ncol = [0,0,99]
    if col[2] > 50:
        ncol = [0,0,10]
    return ncol
    

def get_furthest_color(color_list, att):
    m_light = sum(zip(*color_list)[att])/len(color_list)

    diff = 0
    idx = -1 
    for i in xrange(len(color_list)):
        col = color_list[i]
        d = m_light - col[att]
        if abs(d) > diff:
            diff = d
            idx = i
    f_col = color_list[idx]
    color_list = color_list[:idx] + color_list[idx+1:]
    return f_col, color_list




