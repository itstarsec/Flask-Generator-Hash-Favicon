import mmh3
import requests
import codecs

def test(url):
	response = requests.get(url)
	favicon = codecs.encode(response.content,"base64")
	hashed_int = mmh3.hash(favicon)
	return hashed_int
