#!/usr/bin/python

from bs4 import BeautifulSoup
import sys

filename = ''

def getHTMLContents():
    if not filename:
        print "Need html file"
        sys.exit(0)
    contents = ''
    with open(filename, "rw") as html_fh:
        contents = html_fh.read()
    return contents


def getComponentListWithModule(contents=''):
    data_dict = {}
    lengths = []
    soup = BeautifulSoup(contents)
    i=1
    # tag_dict=soup.findAll(text=True)
    # tag = soup.findAll(text=True);
    # print tag
    # print len(soup.findChildren())
    for word in soup.findChildren():
        if len(word.findChildren())==0:
            text = word.getText()
            if text!='\n' and len(word.getText())!=0 and 'translate' not in word.attrs.keys():
                print text
        # i=i+1
        # if i==16:
        #     # print word.parent
        #     print len(word.getText())
    # for value in soup.findAll('',text=True):
    #     # print type(soup)
    #     print value.__dict__.keys()
    #     # print value.
    #     if value!='\n':
    #         if value.getText():
    #             print value.getText()
    #             #print value.attrs
    #             if 'type' in value.attrs:
    #                 print value.attrs
    #         i=i+1;
    #     print i

        # v=value.__dict__.values()
        # k = value.__dict__.keys()
        # break;
    # pElems = soup.select('button')
    #print v,k
    #print pElems[0].getText()
    # Monkey fix:


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print "Supply HTML file that needs modifications"
        sys.exit(0)
    filename = sys.argv[1]
    getComponentListWithModule(getHTMLContents())
