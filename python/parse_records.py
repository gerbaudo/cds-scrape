#!/bin/env python

# first try at reading the output xml just using the builtin python library
#
# davide.gerbaudo@gmail.com
# 2014-08
#

# Examples:
# get marc21 xml
# wget --load-cookies=cookies.txt -O pub_drafts_hist_cc.xml https://cds.cern.ch/search?ln=en\&p=\&action_search=Search\&op1=a\&m1=a\&p1=\&f1=\&cc=ATLAS+Publication+Drafts+History\&sf=\&so=d\&rm=\&rg=900\&sc=1\&of=xm
# get dublin xml
# wget --load-cookies=cookies.txt -O dublin.xml https://cds.cern.ch/search?ln=en\&cc=ATLAS+Publication+Drafts+History\&p=\&action_search=Search\&op1=a\&m1=a\&p1=\&f1=\&c=ATLAS+Publication+Drafts+History\&c=\&sf=\&so=d\&rm=\&rg=10\&sc=1\&of=xd
import xml
import xml.etree.ElementTree as ET
import collections

def main():
    input_file='dublin.xml'
    tree = ET.parse(input_file)
    root = tree.getroot()
    useless='http://purl.org/dc/elements/1.1/'
    counter = 0
    for child in root:
        # print child.tag,'-->'
        for r in child:
            # print "tag '{0}', attrib '{1}'".format(r.tag, r.attrib)
            if 'title' in r.tag:
                print "[{0}] : {1}".format(counter, r.text)
                counter += 1
# for record in root.findall('collection/record'):
#         print record.tag, record.attrib
if __name__=='__main__':
    main()
