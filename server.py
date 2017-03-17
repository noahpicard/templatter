import os
import sys

from flask import Flask, request, redirect, url_for, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from generate import *
import random
import string
import json

UPLOAD_FOLDER = "./upload"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['APPLICATION_ROOT'] = './static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


source_file = ""

@app.route('/')
def serve_ui():
	""" Serve the ui's html.
	"""
	filename = generate_html_file(source_file)
	return app.send_static_file('introPage.html')

@app.route('/static/submit')
def submit_website():
    return app.send_static_file('submit_website.html')

@app.route('/static/gen', methods=['GET', 'POST'])
def gen(x=None, y=None):
    filename = generate_html_file(source_file)
    return app.send_static_file('index.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/create', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
      if request.form.get('formType', type=str) == "file":
	        # check if the post request has the file part
	        if 'file' not in request.files: 
	            print('No file part')
	            return redirect(request.url)
	        file = request.files['file']
	        # if user does not select file, browser also
	        # submit a empty part without filename
	        if file.filename == '':
	            print('No selected file')
	            return redirect(request.url)
	        if file and allowed_file(file.filename):
	            filename = secure_filename(file.filename)
	            print os.getcwd() 
	            print os.path.join(app.config['UPLOAD_FOLDER'], filename)
	            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	            return redirect(url_for('uploaded_file',
	                                    filename=filename))
      else:
	        siteJson = createSiteJSON()
	        print siteJson
	        filename = './test_data/'+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20)) + ".json"
	        with open(filename,"wb") as fo:
	        	fo.write(siteJson)
	        source_file = filename
	        return filename
  return app.send_static_file('createSite.html')

def createSiteJSON():
		print "Creating JSON!"
		site = {}
		site['title'] = request.form.get('siteTitle', type=str)
		site['subtitle'] = request.form.get('siteSubtitle', type=str)
		content = {}
		content['businessTitle'] = site['title']
		content['businessSubTitle'] = site['subtitle']
		pages = {}
		for i in range(100):
			page = {}
			page["content"] = {}
			pageStr = "page" + str(i)
			if request.form.get(pageStr, type=str) == None:
				break
			page['title'] = request.form.get(pageStr+'Title', type=str)
			page['subtitle'] = request.form.get(pageStr+'Subtitle', type=str)
			page['pageType'] = request.form.get(pageStr+'PageType', type=str)

			# Intro
			intro = {}
			intro['mainImages'] = {} 
			intro['mainImages']['main'] = request.form.get(pageStr+'MainImage', type=str)
			callToAction = {}
			callToAction['heading'] = request.form.get(pageStr+'CTAHeading', type=str)
			callToAction['subheading'] = request.form.get(pageStr+'CTASubheading', type=str)
			callToAction['actionButton'] = request.form.get(pageStr+'CTAActionButton', type=str)
			callToAction['actionLink'] = request.form.get(pageStr+'CTAActionLink', type=str)
			intro['callToAction'] = callToAction
			page['content']['intro'] = intro

			#Details
			details = {}
			sections = {}
			for j in range(100):
				section = {}
				sectionStr = pageStr + "Section" + str(i)
				if request.form.get(sectionStr, type=str) == None:
					break
				section['heading'] = request.form.get(sectionStr+'Heading', type=str)
				section['subheading'] = request.form.get(sectionStr+'Subheading', type=str)
				section['paragraph'] = request.form.get(sectionStr+'Paragraph', type=str)
				section['image'] = request.form.get(sectionStr+'Image', type=str)
				sections[sectionStr] = section
			details['sections'] = sections
			page['content']['details'] = details
			pages[pageStr] = page
		content['pages'] = pages
		footer = {}
		footer['links'] = {}
		content['footer'] = footer
		site['content'] = content
		return json.dumps(site, indent=4, sort_keys=True)



@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

#with app.test_request_context('/gen', method='POST'):
	

if __name__ == '__main__':
	source_file = sys.argv[1]
	app.run(debug=True)