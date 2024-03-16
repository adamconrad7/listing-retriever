import xml.etree.ElementTree as ET

# Given the path of an xml file, a target param to replace, and a value to replace the target with,
# return a url we can make a request to
def get_url(xmlFile, target, val):

    # Parse the XML file
    tree = ET.parse(xmlFile)  
    root = tree.getroot()
    req_list = root[0][8].text.split('\n')
    req_list = list(filter(lambda x: x != '', req_list))
    
    # Parse request from XML
    headers_dict = {}
    for i in req_list[1:]:
        header_name, header_value = i.split(": ", 1)
        headers_dict[header_name] = header_value
    url = 'https://' + headers_dict['Host'] + req_list[0].split(' ')[1]
    url = url.replace(target, val)
    return url, headers_dict


