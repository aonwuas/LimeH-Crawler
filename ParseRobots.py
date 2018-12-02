import re
import urllib2
DISALLOW = r'[Dd]isallow:\s?'

class Parser:

    def __init__(self):
        pass


    # GET site robots.txt
    def get_robots_txt(self, url):
        try:
            req = urllib2.Request(url)
            req.add_header('User-Agent', 'LimeCrawler')
            r = urllib2.urlopen(req).read()
            return r
        except Exception as e:
            print(str(e))

    # External parse request
    def parse(self, url):
        ro_text = self.get_robots_txt(url)
        return self._parse(ro_text)
    
    # Internal parse logic.  Return all lines beginning with Disallow
    def _parse(self, ro_text):
        links = []
        for line in ro_text.split('\n'):
            if re.match(DISALLOW, line):
                links.append(re.sub(DISALLOW, "", line))
        return links


