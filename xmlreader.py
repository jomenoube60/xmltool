import xml.etree.ElementTree as ET
import re
tree = ET.parse('document.xml')
root = tree.getroot()

trimpattern = r'{.*}'
def trimtag(pattern,tag):
    m = re.search(pattern,tag)
    return tag.replace(m.group(0), '')

def get_tag_name(element):
    return trimtag(trimpattern,element.tag)
def get_child(element):
    return [e for e in element]

def getbody():
    pass