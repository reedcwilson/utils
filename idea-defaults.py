#!/usr/bin/env python

import xml.etree.cElementTree as ET
import os
import sys

idea_dir = ''

def get_idea_dir(root_dir):
  if os.path.exists(root_dir):
    dirs = [os.path.join(root_dir, name) for name in os.listdir(root_dir) 
        if name == '.idea' and os.path.isdir(os.path.join(root_dir, name))]
    if not len(dirs) == 1:
      print "didn't find the idea directory"
      sys.exit(1)
    return dirs[0]

# give directory of project and it finds the idea folder
if len(sys.argv) > 1:
  idea_dir = get_idea_dir(sys.argv[1])

# don't give a directory and it assumes current dir contains idea subdir
if len(sys.argv) == 1:
  idea_dir = get_idea_dir(os.path.dirname(os.path.realpath(__file__)))


#===============================================================================
# Workspace Defaults
#===============================================================================

workspace_file = "%s/workspace.xml" % (idea_dir)
tree = ET.parse(workspace_file)

# get all the window info objects and set the auto_hide attr to true
window_infos = tree.getroot().findall('component[@name="ToolWindowManager"]/layout/window_info')
for info in window_infos:
  info.set("auto_hide", 'true')

tree.write(workspace_file)

print "updated defaults"
