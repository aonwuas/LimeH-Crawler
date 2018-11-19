from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import ParseRobots
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
        print("Received POST request")
        content_len = int(self.headers['Content-Length'], 0)
        body = self.rfile.read(content_len)
        # Link analysis asking for robots.txt parse
	if self.path == "/robots":
            self.parseRobotstxt(body)
        # Link Analysis giving link to crawl
        elif self.path == "/crawl":
            print("/crawl")
            self.addUrlToQueue(body)
        # Crawler requesting link from queue
        elif self.path == "/url":
            #print('url endpoint')
            self.sendCrawlerUrl(body)
        else:
            pass
    
    
    def parseRobotstxt(self, body):
        json_string = self.robot_parser.parse(str(body).strip())
        self.q_respond(json_string)
        return
    
    
    def addUrlToQueue(self, body):
        #strip whitespace from link and add to queue
        self.link_list.append(str(body).strip())
        print("\'" + str(body).strip() + "\' added to queue")
        self.q_respond(None)
        return
    
    
    def sendCrawlerUrl(self, body):
        #print("crawler request, links are: ")# + str(self.link_list))
        #print(str(self.link_list))
        json_string = ""
        if(len(self.link_list) > 0):
            link = self.link_list.pop(0)
            #print("sending link to crawler: " + str(link))
            json_string = link
        self.q_respond(json_string)
        return
    
    
    def q_respond(self, json_string):
        self.send_response(200)
        self.end_headers()
        if json_string != None:
            self.wfile.write(json_string)
        return
'''
    def start(self):
        #following snippet taken from https://www.acmesystems.it/python_http
        try:
            #Create a web server and define the handler to manage the
            #incoming request
            server = HTTPServer(('', PORT_NUMBER), CrawlServer)
            print 'Started httpserver on port ' , PORT_NUMBER

            #Wait forever for incoming htto requests
            server.serve_forever()

        except KeyboardInterrupt:
            print '^C received, shutting down the web server'
            server.socket.close()
'''
