from HTMLParser import HTMLParser
import urllib2

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.reset()
        self.data_list = []
        self.i = 0
        self.j = 0
    def handle_starttag(self, tag):
        print 'need to fill in'
    def handle_data(self, data):
        if data.lower() == 'scoring summary':
            print "Scoring Summary"
            self.i = len(self.data_list)
            print self.i
        if data.lower() == 'team stat comparison':
            print "Team Stat Comparison"
            self.j = len(self.data_list)
            print self.j
            
        self.data_list.append(data)
    def get_data(self):
        score_data = self.data_list[self.i:self.j]
        return score_data
        
def data_collector(html):
    parser = MyHTMLParser()
    parser.feed(html)
    return parser.get_data()
                                

page = urllib2.urlopen('http://scores.espn.go.com/ncf/boxscore?gameId=400610325')
html = page.read()

print data_collector(html)

