from flask import Flask, request, jsonify, send_from_directory
import sys
from generate import *

app = Flask(__name__)
app.config['APPLICATION_ROOT'] = './static'

source_file = ""

@app.route('/')
def serve_ui():
	""" Serve the ui's html.
	"""
	filename = generate_html_file(source_file)
	return app.send_static_file('introPage.html')


@app.route('/static/gen', methods=['GET', 'POST'])
def gen(x=None, y=None):
    filename = generate_html_file(source_file)
    return app.send_static_file('index.html')

#with app.test_request_context('/gen', method='POST'):
	

if __name__ == '__main__':
	source_file = sys.argv[1]
	app.run(debug=True)