import json
from jinja2 import Environment, PackageLoader
import generate_navbar
import generate_banner
import generate_sections
import generate_footer
import generate_css
from generate_utils import *

env = Environment(loader=PackageLoader('templates', '.'))

navbar_template_list = [
    'centerDisplayNavbar',
    'basicNavbar',
    'transparentNavbar',
    'fadeOverlayNavbar']

main_image_template_list = [
    'fullCenterImage',
    'colorFullCenterImage']

cta_template_list = [
    'centerCTA',
    'leftCTA',
    'subRightCTA']

section_template_list = [
    'columnSection',
    # 'zigSection',
    'thinZigSection',
    'mixOneTwoSection',
    'bandZigSection']

footer_template_list = [
    'basicFooter']


def generate_html_file(source_file):
    with open(source_file) as data_file:
        data = json.load(data_file)

    data_pages = data['content']['pages']
    menu_links = [page_title for page_title in data_pages]

    navbar, navbar_template = generate_navbar.generate_navbar(env, navbar_template_list, data, menu_links)

    footer, footer_template = generate_footer.generate_footer(env, footer_template_list, data)

    section_templates = []

    for page_title in data_pages:
        page = data_pages[page_title]

        page_content, section_template = generate_page_content(page)

        section_templates.append(section_template)

        content = navbar + page_content + footer

        result = env.get_template('emptyPage.html').render(title=data["title"], content=content)

        make_file('static/' + page_title + '.html', [result])

    print "navbar:", navbar_template
    print "sections:", section_templates
    print "footer:", footer_template
    print generate_css.generate_css_file(env, data, navbar_template, footer_template, section_templates)

    return generate_intro_page(data, menu_links)


def generate_page_content(data):
    page_content = []
    section_template = ""

    if 'pageType' in data:
        pageType = data['pageType']

    if 'content' in data:
        content = data['content']
        if 'intro' in content:
            intro = content['intro']
            if 'mainImages' in intro:
                mainImages = intro['mainImages']
                img_index = 0
                for image in mainImages:
                    img_content = ''
                    if img_index == 0:
                        img_content = generate_banner.generate_cta(env, cta_template_list, intro)
                    page_content.append(generate_banner.generate_main_image(env, main_image_template_list, mainImages[image], img_content))
                    img_index += 1
                    break
        if 'details' in content:
            details = content['details']
            if 'sections' in details:
                detail_sections = details['sections']
                temp_detal_sections, section_template = generate_sections.generate_detail_sections(env,
                                                                                                   section_template_list,
                                                                                                   detail_sections)
                page_content.append(temp_detal_sections)
    return "\n".join(page_content), section_template


def generate_intro_page(data, menu_links):
    navbar = env.get_template('navbar/basicNavbar.html').render(
        business_title="<br/>" + data['content']['businessTitle'],
        business_subtitle=data['content']['businessSubTitle'],
        links=["static/" + link for link in menu_links])

    content = navbar + """
	<br>

	<a href="/static/gen">Generate new layout!</a>
	"""

    result = env.get_template('emptyPage.html').render(title=data["title"], content=content)
    make_file('static/introPage.html', [result])
