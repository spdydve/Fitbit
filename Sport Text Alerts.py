from HTMLParser import HTMLParser
import urllib2

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.reset()
        self.data_list = []
        self.i = 0
        self.j = 0

    def handle_data(self, data):
        print "Encountered some data  :", data
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


page = urllib2.urlopen('https://rdcrnqa.epi.usf.edu//rdnwebapp/Forms/05VCRC/5532/RecurringMedications.aspx?EventScheduleId=12658&RdcrnProtocolId=5532&ProtocolId=363&creguid=1697&trimester=4')
html = page.read()

print data_collector(html)

# Hello