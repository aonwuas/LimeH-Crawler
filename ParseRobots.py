import re
import urllib2
DISALLOW = r'^[Dd]isallow:\s?'
USER_AGENT = r'^[Uu]ser-[Aa]gent:'

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
        print(url)
        ro_text = self.get_robots_txt(url)
        return self._parse(ro_text)
    
    # Internal parse logic.  Return all lines beginning with Disallow
    def _parse(self, ro_text):
        links = []
        prev = ""
        for line in ro_text.split('\n'):
            if re.match(DISALLOW, line) and not re.match(USER_AGENT, prev):
                links.append(re.sub(DISALLOW, "", line))
            prev = line
        #json = '{\n\t"Disallowed": ' + str(links) + '\n}'
        #print("====Parsed Robots JSON====")
        #print(json)
        #print("=========End JSON=========\n")
        return links

    def valid_useragent(line):
        return true


