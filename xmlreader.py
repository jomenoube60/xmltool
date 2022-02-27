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

def get_children(element , filter= None):
    if filter == None:
        return [e for e in element]
    else:
        return [e for e in element if filter == get_tag_name(e)]

def iterate_through(fn,elm):
    i = 0 
    while i < len(elm):
        fn(elm[i])
        iterate_through(fn,elm[i])            
        i += 1

def get_element_by_tag_name(tagname):
    result = []
    def sendtoresult(elm):
        if get_tag_name(elm) == tagname:
            result.append(elm)
    iterate_through(sendtoresult ,root)
    return result
        