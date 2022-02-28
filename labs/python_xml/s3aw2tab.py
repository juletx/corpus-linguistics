#!/usr/bin/python3

import sys
from lxml import etree

# create a tabulated file from s3aw.xml
# the output of the file is:
#
# token_id TAB token_pos TAB token_form TAB token_sense
#
# Notes:
#
#        - discard instances with no id
#        - discard instances with no pos
#        - discard instances with no senses
#        - if word has more than one possible sense, output just the first one

if len(sys.argv) != 2:
    print ("Usage: python3 " + sys.argv[0] + " s3aw.xml > s3aw.tab")
    exit(1)

fname = sys.argv[1]
parser = etree.XMLParser(remove_blank_text=True) # discard whitespace nodes
tree = etree.parse(fname, parser)

for token_elem in tree.xpath("/context/s/token"):
    # Use:
    #
    # elem.get("...") -> get attribute
    #                    returns None if attribute does not exist
    #
    # elem.text       -> get textual content
    #

    token_id = token_elem.get("id")
    if token_id is None:
        continue
    token_pos = token_elem.get("pos")
    if token_pos is None:
        continue
    token_wf = token_elem.findtext("wf")
    token_sense = token_elem.findtext("lexsn")
    if token_sense is None:
        continue
    output_string = "{}\t{}\t{}\t{}".format(token_id, token_pos, token_wf, token_sense)
    print(output_string)
