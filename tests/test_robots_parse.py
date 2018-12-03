import sys
sys.path.append('../')
import ParseRobots

def testParse():
    p = ParseRobots.Parser()
    try:
        p.parse("https://www.google.com/robots.txt")
    except ExceptionType:
        self.fail("parse function failed")
