from generate_utils import *


def generate_main_image(env, main_image_template_list, img_url, img_content):
    main_image_template = pick_one(main_image_template_list)
    return env.get_template('fullimage/' + main_image_template + '.html').render(image_url=img_url, content=img_content)


def generate_cta(env, cta_template_list, data):
    if 'callToAction' in data:
        cta_template = pick_one(cta_template_list)
        cta = data['callToAction']
        return env.get_template('cta/' + cta_template + '.html').render(heading=cta['heading'],
                                                                        subheading=cta['subheading'],
                                                                        action_link=cta['actionLink'],
                                                                        action_button=cta['actionButton'])
    return ''