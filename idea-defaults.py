import xml.etree.cElementTree as ET
import sys

filename = sys.argv[1]
tree = ET.parse(filename)

# get all the window info objects and set the auto_hide attr to true
window_infos = tree.getroot().findall('component[@name="ToolWindowManager"]/layout/window_info')
for info in window_infos:
  info.set("auto_hide", 'true')

tree.write(filename)
