from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import ParseRobots
from jsonizer import jsonize
# True port # is 80
# PORT_ NUMBER = 80

PORT_NUMBER = 8080

class CrawlServer(BaseHTTPRequestHandler):
    link_list = [] 
    robot_parser = None

    #Handle POST requests
    def do_POST(self):
        if self.robot_parser == None:
            self.robot_parser = ParseRobots.Parser()
        #print("Received POST request")
        content_len = int(self.headers['Content-Length'], 0)
        body = self.rfile.read(content_len)
        # Link analysis asking for robots.txt parse
	if self.path == "/robots":
            self.parse_robots_txt(body)
        # Link Analysis giving link to crawl
        elif self.path == "/crawl":
            self.add_url_to_queue(body)
        # Crawler requesting link from queue
        elif self.path == "/url":
            self.send_crawler_url(body)
        else:
            pass
    
# Override message BaseHTTPRequestHandler logging function to ignore internal API calls
    def log_message(self, format, *args):
        try:
            if('url'in args[0]):
                pass
            else:
                BaseHTTPRequestHandler.log_message(self, format, *args)
            return
        except Exception as e:
            print(e)

    def parse_robots_txt(self, body):
        json_string = self.robot_parser.parse(str(body).strip())
        json_string = '{\n\tDisallowed: ' + str(json_string) + '\n}'
        self.q_respond(json_string)
        return
    
    
    def add_url_to_queue(self, body):
        # { 'URLs': ['url1', 'url2', 'url3', 'url4'] }
        url_list = jsonize(body)['URLs']
        self.link_list.extend(url_list)
        self.q_respond(None)
        return
    
    
    def send_crawler_url(self, body):
        url = ""
        if(len(self.link_list) > 0):
            link = self.link_list.pop(0)
            url = link
        self.q_respond(url)
        return

    
    def q_respond(self, json_string):
        self.send_response(200)
        self.end_headers()
        if json_string != None:
            self.wfile.write(json_string)
        return

