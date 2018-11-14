import sys
from CrawlServer import CrawlServer
from Crawler import Crawler


# Usage python LimeCrawler [python LimeCrawler.py port* num_crawlers*]
# *optional args
if __name__ == "__main__":
        port = 8080
        num_crawlers = 1
        if len(sys.argv) == 2:
            port = sys.argv[1]
        elif len(sys.argv) == 3:
            port = sys.argv[1]
            num_crawlers = sys.argv[2]

	# Start CrawlServer
        server = CrawlServer(port)
	# Start Crawler(s)
        # Create SendSer Object
        pass
