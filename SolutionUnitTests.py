import unittest
import re
from pythonSolution import DataExtractor, WebsitePage, TimeLapse, Summary
class DataExtractorTestCase(unittest.TestCase):
	
	def setUp(self):
		self.de = DataExtractor()

	def test_url_regex_setup(self):
		url_regex = re.compile('href="[\w&.\-?/:=]+"')
		self.assertEqual(self.de._url_pattern, url_regex)

	def test_extract_all_uri(self):
		uri1 = "//b.scorecardresearch.com"
		uri2 = "http://finance.yahoo.com/currency-converter"
		uri3 = "htpp://abcd.com/q?e=opq"
		html = '<html><a href="'+uri1+'"><a href="'+uri2+'"><a href="'+uri3+'"><\html>'
		result_uris = self.de.extract_all_uri(html)
		expectde_uris = [uri1,uri2,uri3]
		self.assertEqual(expectde_uris, result_uris)

from mock import MagicMock, Mock
import urllib, sys
class WebsitePageTestCase(unittest.TestCase):

	def setUp(self):
		uri1 = "//b.scorecardresearch.com"
		uri2 = "http://finance.yahoo.com/currency-converter"
		uri3 = "htpp://abcd.com/q?e=opq"
		self.html = '<html><a href="'+uri1+'"><a href="'+uri2+'"><a href="'+uri3+'"><\html>'
		self.page = MagicMock()
		self.page.read.return_value = self.html
		self.page.info.return_value = {"salkf" : "jfakhak"}
		urllib.urlopen = MagicMock(return_value = self.page)
	
	def test_web_page_setup(self):
		address = "http://finance.yahoo.com"
		wp = WebsitePage(address)
		urllib.urlopen.assert_called_once_with(address)
		self.assertEqual(self.page, wp.page)

	def test_webpage_html(self):
		wp = WebsitePage("http://finance.yahoo.com")		
		self.assertEqual(self.html, wp.read())

	def test_webpage_info(self):
		wp = WebsitePage("http://finance.yahoo.com")		
		self.assertEqual( {"salkf" : "jfakhak"}, wp.info())

	def test_webpage_download_size(self):
		self.page.info.return_value = {"Content-Length" : 100}
		wp = WebsitePage("http://finance.yahoo.com")
		self.assertEqual(100, wp.download_size())

	def test_webpage_download_size_Content_Lenght_not_present(self):
		wp = WebsitePage("http://finance.yahoo.com")
		self.assertEqual(sys.getsizeof(self.html), wp.download_size())


from datetime import datetime
class TimeLapseTestCase(unittest.TestCase):

	def test_start_time_initialized_to_now(self):
		now = datetime.now().replace(microsecond=0)
		self.assertEqual(now, TimeLapse().start_time)

	def test_time_lapsed(self):
		tl = TimeLapse()
		end_time = datetime.now().replace(microsecond=0)
		expected_time_lapsed = end_time - tl.start_time
		self.assertEqual(expected_time_lapsed, tl.time_lapsed())

class SummaryTestCase(unittest.TestCase):

	def test_print_summary(self):
		s = Summary()
		s.download_size = 100
		s.urls = []
		s.time_required = 40
		s.error = None
		result_string = s.to_string()
		self.assertIn("Download Size is 100", result_string)
		self.assertIn("Urls is []", result_string)
		self.assertIn("Time Required is 40", result_string)


if __name__ == '__main__':
    unittest.main()