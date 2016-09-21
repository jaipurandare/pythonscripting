import urllib
import sys
class WebsitePage():

	def __init__(self, website_address):
		self.page =  urllib.urlopen(website_address)
	
	def read(self):
		return self.page.read()

	def info(self):
		return self.page.info()

	def download_size(self):
		info = self.page.info()
		if "Content-Length" in info.keys(): 
			return self.page.info()["Content-Length"]
		else:
			return sys.getsizeof(self.page)

import re
class DataExtractor():
	
	def __init__(self):
		self._url_pattern = re.compile('href="[\w&.\-?/:=]+"')

	def extract_all_uri(self, html):
		urls = re.findall(self._url_pattern, html)
		return map(self._clean_uri, urls)

	def _clean_uri(self, href_string):
		return href_string.split('"')[1]


from datetime import datetime
class TimeLapse():

	def __init__(self):
		self.start_time = self._get_time_now()

	def time_lapsed(self):
		return self._get_time_now() - self.start_time

	def _get_time_now(self):
		return datetime.now().replace(microsecond=0)


class Summary():

	def __init__(self):
		self.urls = None
		self.time_required = None
		self.download_size = None
		self.error = None

	def to_string(self):
		info = []
		params = self.__dict__
		for k,v in params.iteritems():
			string = "{0} is {1}".format(k.replace("_"," ").title(), v)
			if (None != v): info.append(string) 
		return "\n".join(info)



def main():
	website_address = "http://finance.yahoo.com/"
	summary = Summary()
	try:
		tl = TimeLapse()
		wp = WebsitePage(website_address)
		de = DataExtractor()
		html = wp.read()
		summary.urls = de.extract_all_uri(html)
		summary.download_size = wp.download_size()
		summary.time = tl.time_lapsed()
	except IOError, e:
		print e
		# summary.error = {"type" : IOError.type, "message": "Could not open website"}
		summary.error = e
	except Exception, e:
		print e
		summary.error = e
	print summary.to_string()

if __name__ == "__main__":
	main() 