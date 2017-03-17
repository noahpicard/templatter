import generate_fonts
import generate_colors
from generate_utils import *

def generate_css_file(env, data, navbar_template="", footer_template="", section_templates=[]):
    primary_color, secondary_color, accent_color, text_color, inv_text_color = generate_colors.get_color_set()
    heading_font, content_font = generate_fonts.get_font_set()

    result = env.get_template('basicBody.css').render(primary_color=primary_color,
                                                      secondary_color=secondary_color, text_color=text_color,
                                                      accent_color=accent_color,
                                                      inv_text_color=inv_text_color,
                                                      heading_font=heading_font, content_font=content_font)

    navbarcss = ""
    if navbar_template in ['centerDisplayNavbar', 'transparentNavbar', 'fadeOverlayNavbar']:
        navbarcss = env.get_template('navbar/' + navbar_template + '.css').render(primary_color=primary_color,
                                                                                  secondary_color=secondary_color,
                                                                                  text_color=text_color,
                                                                                  accent_color=accent_color,
                                                                                  inv_text_color=inv_text_color,
                                                                                  heading_font=heading_font,
                                                                                  content_font=content_font)

    footercss = ""
    if footer_template in []:
        footercss = env.get_template('footer/' + footer_template + '.css').render(primary_color=primary_color,
                                                                                  secondary_color=secondary_color,
                                                                                  text_color=text_color,
                                                                                  accent_color=accent_color,
                                                                                  inv_text_color=inv_text_color,
                                                                                  heading_font=heading_font,
                                                                                  content_font=content_font)

    sectioncss = ""
    for section_template in section_templates:
        if section_template in ['thinZigSection']:
            sectioncss += env.get_template('section/' + section_template + '.css').render(primary_color=primary_color,
                                                                                          secondary_color=secondary_color,
                                                                                          text_color=text_color,
                                                                                          accent_color=accent_color,
                                                                                          inv_text_color=inv_text_color,
                                                                                          heading_font=heading_font,
                                                                                          content_font=content_font)

    return make_file('static/css/style.css', [result, navbarcss, footercss, sectioncss])