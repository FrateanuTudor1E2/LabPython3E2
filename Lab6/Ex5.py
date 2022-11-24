import re

def xml_dict(path_to_xml, attrs):
    result = []
    with open(path_to_xml, "r") as f_d:
        for el in re.findall("<\w+.*?>", f_d.read()):
            if (any([re.search(item[0] + "\s*=\s*\"" + item[1] + "\"", el, flags=re.I) for item in attrs.items()])):
                result += [el]
    return result

attrs={"class": "url", "name": "url-form", "data-id": "item"}
path_to_xml="C:\\Users\\tudor\\PycharmProjects\\LabPython3E2\\Lab6\\file.xml"
print(xml_dict(path_to_xml,attrs))