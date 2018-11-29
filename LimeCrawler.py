import sys
import subprocess
from CrawlServer import CrawlServer
from Crawler import Crawler
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

URL = 'http://lime-h.cs.rpi.edu'

# Usage python LimeCrawler [python LimeCrawler.py port* num_crawlers*]
# *optional args
if __name__ == "__main__":
        # Kill apache2 to free up port 80
        #subprocess.call("./stop.sh")
        port = 80
        num_crawlers = 1
        crawlers = []
        if len(sys.argv) == 2:
            port = int(sys.argv[1])
        elif len(sys.argv) == 3:
            port = int(sys.argv[1])
            num_crawlers = int(sys.argv[2])

        # url endpoint for crawler to request link
        url = URL + ":" + str(port) + "/url"
        for i in range(0, num_crawlers):
            crawler = Crawler(i, url)
            crawler.start()
            crawlers.append(crawler)


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
