#!/usr/bin/python

from xml.dom import minidom

doc = minidom.parse('V8dump.xml')

services = doc.getElementsByTagName('service')

print('<?xml version="1.0" encoding="utf-8"?>')
print('<resources>')

item1 = '        <item>'
item2 = '</item>'

print('    <string-array name="inmotion_services">')
for svc in services:
    svcval = svc.attributes['uuid'].value
    print(item1 + svcval.replace("-","_") + item2)
print('    </string-array>\n')
    
for svc in services:
    svcval = svc.attributes['uuid'].value
    print('    <string-array name="inmotion_' + svcval.replace("-","_") + '">')
    chars = svc.getElementsByTagName('characteristic')
    for char in chars:
        charval = char.attributes['uuid'].value
        print(item1 + charval.replace("-","_") + item2)
    print('    </string-array>\n')

print('</resources>')
