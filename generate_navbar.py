from generate_utils import *


def generate_navbar(env, navbar_template_list, data, menu_links):
    navbar_template = pick_one(navbar_template_list)
    navbar = env.get_template('navbar/' + navbar_template + '.html').render(
        business_title=data['content']['businessTitle'],
        business_subtitle=data['content']['businessSubTitle'],
        links=menu_links)

    return navbar, navbar_template
