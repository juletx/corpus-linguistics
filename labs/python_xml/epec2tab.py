#!/usr/bin/python3

import sys
from lxml import etree

# create a tabulated file from epec_words.xml
# the output of the file is:
#
# token_id TAB token_form
#

if len(sys.argv) != 2:
    print ("Usage: python3 " + sys.argv[0] + " epec_words.xml > epec_words.tab")
    exit(1)

fname = sys.argv[1]
parser = etree.XMLParser(remove_blank_text=True) # discard whitespace nodes
tree = etree.parse(fname, parser)

for w_elem in tree.xpath("put_your_xpath_here"):
    # Use:
    #
    # elem.get("...") -> get attribute
    #                    returns None if attribute does not exist
    #
    # elem.text       -> get textual content
    #

    token_id = ...
    token_form = ...
    output_string = "{}\t{}".format(token_id, token_form)
    print(output_string)
