from HTMLParser import HTMLParser
import urllib2

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.reset()
        self.data_list = []
        self.i = 0
        self.j = 0
    #def handle_starttag(self, tag, attrs):
        #print "Encountered a start tag:", tag
    #def handle_endtag(self, tag):
        #print "Encountered an end tag :", tag
    def handle_data(self, data):
        #print "Encountered some data  :", data
        self.data_list.append(data)
        if data.lower() == 'scoring summary':
            print "Found"
            self.i = len(self.data_list)
            self.data_list.append(data)
        if data.lower() == 'team stat comparison':
            print "Found 2"
            self.j = len(self.data_list)
    def get_data(self):
        print self.i, self.j
        return self.data_list()     
                                
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

page = urllib2.urlopen('http://scores.espn.go.com/ncf/boxscore?gameId=400610325')
html = page.read()

parser.feed(html)
