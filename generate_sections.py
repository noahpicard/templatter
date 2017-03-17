from generate_utils import *
from random import randrange


def generate_detail_sections(env, section_template_list, detail_sections):
    section_weights = {section_name: get_section_size(detail_sections[section_name]) for section_name in
                       detail_sections}
    section_weights = {section_name: section_weights[section_name] / min(section_weights.values()) for section_name in
                       section_weights}
    # bruhsky
    full_sections = []
    counter = 0
    section_row = []
    section_template = pick_one(section_template_list, 2)
    seed = randrange(0, 144)

    for section_name in detail_sections:
        weight = section_weights[section_name]
        section = detail_sections[section_name]
        if 'subheading' not in section:
            section['subheading'] = ''
        section_row.append(env.get_template('section/' + section_template + '.html').render(heading=section['heading'],
                                                                                            subheading=section[
                                                                                                'subheading'],
                                                                                            paragraph=section[
                                                                                                          'paragraph'][
                                                                                                      :250],
                                                                                            image=section['image'],
                                                                                            column_weight='col-md-4',
                                                                                            action_link='#',
                                                                                            counter=counter,
                                                                                            seed=seed,
                                                                                            number_of_sections=len(
                                                                                                detail_sections)))
        print counter, len(detail_sections)
        counter += 1
    full_sections += section_row
    return "\n".join(full_sections), section_template


def get_section_size(section):
    total = 0
    if 'heading' in section:
        total += len(section['heading']) * 7
    if 'subheading' in section:
        total += len(section['subheading']) * 5
    if 'paragraph' in section:
        total += len(section['paragraph'])
    if 'image' in section:
        total += 100
    return total