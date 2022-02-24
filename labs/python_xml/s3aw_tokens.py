#!/usr/bin/python3
from lxml import etree
parser = etree.XMLParser(remove_blank_text=True) # discard whitespace nodes
tree = etree.parse("s3aw.xml", parser) # parse document
# using the tree root as current node, execute the XPath query '//w/text()'
for wftext_elem in tree.xpath("//wf"):
    token = wftext_elem.text
    print(token)
