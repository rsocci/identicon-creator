from identicon import render_identicon
from StringIO import StringIO

CACHE = {}

def cache_check(key):
	return CACHE.get(key)

def cache_set(key, value):
	CACHE[key] = value

def create_identicon(code, size, img_format):
	size = size/3
	img = render_identicon(code, size)
	stream = StringIO()

	img.save(stream, format = img_format)

	return stream

