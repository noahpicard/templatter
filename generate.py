import random
import json
from pprint import pprint
from jinja2 import Template
from jinja2 import Environment, PackageLoader
from random import *
import getcolor as gc

env = Environment(loader=PackageLoader('templates', '.'))

main_image_template_list = ['fullCenterImage.html', 'colorFullCenterImage.html']
navbar_template_list = ['centerDisplayNavbar', 'basicNavbar']
section_template_list = ['columnSection','zigSection','thinZigSection']
footer_template_list = ['basicFooter']
cta_template_list = ['centerCTA', 'leftCTA', 'subRightCTA']
heading_font_list = ['Helvetica Neue', 
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
content_font_list = ['Helvetica Neue', 
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


def generate_html_file(source_file):
	with open(source_file) as data_file:    
		data = json.load(data_file)

	dataPages = data['content']['pages']
	menuLinks = [ page_title for page_title in dataPages ]

	navbar, navbar_template = generate_navbar(data, menuLinks)

	footer, footer_template = generate_footer(data)
	
	section_templates = []

	for page_title in dataPages:
		page = dataPages[page_title]

		page_content, section_template = generate_page_content(page)

		section_templates.append(section_template)

		content = navbar + page_content + footer

		result = env.get_template('emptyPage.html').render(title=data["title"], content=content)

		make_file('static/'+page_title+'.html', [result])

	print generate_css_file(data, navbar_template, footer_template, section_templates)
	print 'broWhat'

	return make_intro_page(data, menuLinks)


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
						img_content = generate_cta(intro)
					page_content.append(generate_main_image(image, mainImages[image], img_content))
					img_index += 1
					break
		if 'details' in content:
			details = content['details']
			if 'sections' in details:
				detail_sections = details['sections']
				temp_detal_sections, section_template = generate_detail_sections(detail_sections)
				page_content.append(temp_detal_sections)
	return "\n".join(page_content), section_template


def generate_detail_sections(detail_sections):
	section_weights = {section_name: get_section_size(detail_sections[section_name]) for section_name in detail_sections}
	section_weights = {section_name: section_weights[section_name]/min(section_weights.values()) for section_name in section_weights}
	#bruhsky
	full_sections = []
	counter = 0
	section_row = []
	section_template = pick_one(section_template_list)
		
	for section_name in detail_sections:
		weight = section_weights[section_name]
		section = detail_sections[section_name]
		if 'subheading' not in section:
			section['subheading'] = ''
		section_row.append(env.get_template(section_template+'.html').render(heading=section['heading'], 
				subheading=section['subheading'], 
				paragraph=section['paragraph'], 
				image=section['image'],
				column_weight='col-md-4',
				action_link='#',
				counter=counter))
		#if counter%4 == 0:
		#	row = "\n".join(section_row)
		#	full_sections.append(#TODO)
		counter += 1
	full_sections += section_row
	return "\n".join(full_sections), section_template


def get_section_size(section):
	total = 0
	if 'heading' in section:
		total += len(section['heading'])*7
	if 'subheading' in section:
		total += len(section['subheading'])*5
	if 'paragraph' in section:
		total += len(section['paragraph'])
	if 'image' in section:
		total += 100
	return total


def generate_main_image(img_name, img_url, img_content) :
	main_image_template = pick_one(main_image_template_list)
	return env.get_template(main_image_template).render(image_url = img_url, content=img_content)


def generate_navbar(data, menuLinks):
	navbar_template = pick_one(navbar_template_list)
	navbar = env.get_template(navbar_template+'.html').render(business_title=data['content']['businessTitle'],
			business_subtitle=data['content']['businessSubTitle'],
			links=menuLinks)

	return navbar, navbar_template


def generate_footer(data):
	footer_template = pick_one(footer_template_list)
	footer = env.get_template(footer_template+'.html').render(business_title=data['content']['businessTitle'],
			business_subtitle=data['content']['businessSubTitle'],
			links=data['content']['footer']['links'])

	return footer, footer_template


def generate_cta(data):
	if 'callToAction' in data:
		cta_template = pick_one(cta_template_list)
		cta = data['callToAction']
		return env.get_template(cta_template+'.html').render(heading = cta['heading'], 
			subheading = cta['subheading'],
			action_link = cta['actionLink'],
			action_button = cta['actionButton'])
	return ''


def pick_one(l, pos=-1):
	if pos != -1:
		return l[pos]
	return l[randint(0, len(l)-1)]


def get_color_set():
	primary_color = '#331177'
	secondary_color='#224477'
	accent_color='#bb192a'
	text_color='#eee'

	colors = gc.get_colors()
	print colors
	print 'Colors len:',len(colors)
	print colors[0][2][2]

	if len(colors) == 2:
		primary_color = colors[0][0]
		secondary_color = colors[1][0]
		if colors[0][2][2] > 50:
			text_color='#222'

	elif len(colors) == 3:
		primary_color = colors[0][0]
		secondary_color = colors[1][0]
		accent_color = colors[2][0]
		if colors[0][2][2] > 50:
			text_color='#222'

	elif len(colors) == 4:
		primary_color = colors[1][0]
		secondary_color = colors[2][0]
		accent_color = colors[3][0]
		if colors[1][2][2] > 50:
			text_color='#222'

	return primary_color, secondary_color, accent_color, text_color


def get_font_set():
	heading_font = pick_one(heading_font_list)
	content_font = pick_one(content_font_list)

	return heading_font, content_font


def generate_css_file(data, navbar_template="", footer_template="", section_templates=[]):
	primary_color, secondary_color, accent_color, text_color = get_color_set()
	heading_font, content_font = get_font_set()

	result = env.get_template('basicBody.css').render(primary_color=primary_color, 
			secondary_color=secondary_color, text_color=text_color, accent_color=accent_color,
			heading_font=heading_font, content_font=content_font)

	navbarcss = ""
	if navbar_template in ['centerDisplayNavbar']:
		navbarcss = env.get_template(navbar_template+'.css').render()
	elif randint(0,1) == 0:
		navbarcss = env.get_template('transparentNavbar.css').render()

	footercss = ""
	if footer_template in []:
		footercss = env.get_template(footer_template+'.css').render()

	sectioncss = ""
	for section_template in section_templates:
		if section_template in ['thinZigSection']:
			sectioncss += env.get_template(section_template+'.css').render()

	return make_file('static/css/style.css', [result, navbarcss, footercss, sectioncss])


def make_intro_page(data, menuLinks):
	navbar = env.get_template('basicNavbar.html').render(business_title="<br/>"+data['content']['businessTitle'],
			business_subtitle=data['content']['businessSubTitle'],
			links=["static/"+link for link in menuLinks])

	content = navbar + """
	<br>

	<a href="/static/gen">Generate new layout!</a>

	<frameset rows="10%,80%,10%">
   <frame name="top" src="../top_frame.htm" />
   <frame name="main" src="index.html" />
   <frame name="bottom" src="../bottom_frame.htm" />
   <noframes>
   <body>
      Your browser does not support frames.
   </body>
   </noframes>
</frameset>
	"""

	result = env.get_template('emptyPage.html').render(title=data["title"], content=content)
	make_file('static/introPage.html', [result])	


def make_file(filename, contents):
	print filename
	with open(filename,'w') as output_file:
		for line in contents:
			output_file.write(line+'\n')
	return filename