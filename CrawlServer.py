from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# True port # is 80
# PORT_ NUMBER = 80

PORT_NUMBER = 8080

class CrawlServer(BaseHTTPRequestHandler):
    
    #Handle POST requests
    def do_POST(self):
        print("Received POST request")
        content_len = int(self.headers['Content-Length'], 0)
        body = self.rfile.read(content_len)
        # Link analysis asking for robots.txt parse
	if self.path == "/robots":
            self.parseRobotstxt(body)
        # Link Analysis giving link to crawl
        elif self.path == "/crawl":
            self.addUrlToQueue(body)
        # Crawler requesting link from queue
        elif self.path == "/url":
            #print('url endpoint')
            self.sendCrawlerUrl(body)
        else:
            pass
    
    
    def parseRobotstxt(self, body):
        #print("/robots\nGot: " + body)
        json_string = 'Parsed robots.txt links'
        self.q_respond(json_string)
        return
    
    
    def addUrlToQueue(self, body):
        #print("/crawl\nGot: " + body)
        self.q_respond(None)
        return
    
    
    def sendCrawlerUrl(self, body):
        print("/url\tGot: " + body)
        json_string = "https://stackoverflow.com"
        self.q_respond(json_string)
        return
    
    
    def q_respond(self, json_string):
        print('respond')
        self.send_response(200)
        #print('end headers')
        self.end_headers()
        #try:
        #    print("try")
        if json_string != None:
            self.wfile.write(json_string)
        #except Exception as e:
        #    print(str(e))
        print('end respond')
        return

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

