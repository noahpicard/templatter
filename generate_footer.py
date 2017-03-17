from generate_utils import *


def generate_footer(env, footer_template_list, data):
    footer_template = pick_one(footer_template_list)
    footer = env.get_template('footer/' + footer_template + '.html').render(
        business_title=data['content']['businessTitle'],
        business_subtitle=data['content']['businessSubTitle'],
        links=data['content']['footer']['links'])

    return footer, footer_template