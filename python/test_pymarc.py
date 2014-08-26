#!/bin/env python


# -- install pymarc:
# virtualenv test
# cd test/
# source bin/activate
# cd ..
# pip install pymarc
# 

# -- get the data
# wget --load-cookies=cookies.txt -O pub_drafts_hist.xml https://cds.cern.ch/search?ln=en\&p=\&action_search=Search\&op1=a\&m1=a\&p1=\&f1=\&cc=ATLAS+Publication+Drafts+History\&sf=\&so=d\&rm=\&rg=900\&sc=1\&of=xm
# -- format
# iconv -f utf8 -t ascii//TRANSLIT  pub_drafts_hist.xml | dos2unix | tr -d '\015' | tr -d '\013' > /tmp/gerbaudo/foo.xml
# -- run, see broken line, delete it
# sed -n '20953p' /tmp/gerbaudo/foo.xml
# sed -i '20953d' /tmp/gerbaudo/foo.xml
# -- run
# ./test_pymarc.py > titles.txt

import pymarc

xml_file='/afs/cern.ch/user/g/gerbaudo/tmp/cds-scrape/foo_ascii.xml'
xml_file='/afs/cern.ch/user/g/gerbaudo/tmp/cds-scrape/pub_drafts_ascii.new.xml'
xml_file='/tmp/gerbaudo/foo.xml'
records = pymarc.parse_xml_to_array(xml_file)
for i, record in enumerate(records):
    # if i>10 : break
    comments_fields = record.get_fields('773')
    num_comments=None
    if len(comments_fields)==1:
        num_comments = int(comments_fields[0].value())
    # print [f.value() for f in record.get_fields('773')]
  # <datafield tag="773" ind1=" " ind2=" ">
  #   <subfield code="p">9</subfield>

    print "[{0}] {1} {2}".format(i, num_comments, record.title())
