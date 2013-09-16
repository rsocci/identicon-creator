from flask import Flask, render_template, Response, \
request, abort, send_file
from binascii import hexlify

import utils

app = Flask('identicons')

SUPPORTED_FORMATS = ['jpeg', 'png']

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/api/identicon/')
@app.route('/api/identicon/<text>')
def indenticon(text=None):
	if not text:
		return send_file('static/img/placeholder.jpg')

	try:
		size = int(request.args.get('size', 100))
	except ValueError:
		abort(400)

	img_format = request.args.get('format', 'jpeg').lower()

	if img_format not in SUPPORTED_FORMATS:
		abort(400)
	
	key = '-'.join([text, str(size), img_format])
	cached_icon = utils.cache_check(key)

	if cached_icon:
		data = cached_icon
	else:
		code = int(hexlify(text), 16)
		stream = utils.create_identicon(code, size, img_format)
		data = stream.getvalue()

		stream.close()
		utils.cache_set(key, data)

	response = Response(data, mimetype='image/' + img_format)
	return response

if __name__ == '__main__':
	app.run(debug=True)