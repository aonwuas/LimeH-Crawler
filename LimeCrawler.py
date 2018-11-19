import sys
from CrawlServer import CrawlServer
from Crawler import Crawler
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

URL = 'http://lime-h.cs.rpi.edu'

# Usage python LimeCrawler [python LimeCrawler.py port* num_crawlers*]
# *optional args
if __name__ == "__main__":
        port = 8081
        num_crawlers = 1
        crawlers = []
        if len(sys.argv) == 2:
            port = int(sys.argv[1])
        elif len(sys.argv) == 3:
            port = int(sys.argv[1])
            num_crawlers = int(sys.argv[2])

        #Start CrawlServer
        #server = CrawlServer(port)
	# Start Crawler(s)
        url = URL + ":" + str(port) + "/url"
        for i in range(0, num_crawlers):
            crawler = Crawler(i, url)
            crawler.start()
            crawlers.append(crawler)
        # Create SendSer Object


        #following snippet taken from https://www.acmesystems.it/python_http
        try:
            #Create a web server and define the handler to manage the
            #incoming requests
            server = HTTPServer(('', port), CrawlServer)
            print 'Started httpserver on port ' , port

            #Wait forever for incoming htto requests
            server.serve_forever()

        except KeyboardInterrupt:
           print '^C received, shutting down the web server'
           server.socket.close()
