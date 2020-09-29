#!/usr/bin/env python

import xml.etree.cElementTree as ET
import os
import sys
import shutil

idea_dir = ''


def get_idea_dir(root_dir):
    if os.path.exists(root_dir):
        dirs = [
                os.path.join(root_dir, name)
                for name in os.listdir(root_dir)
                if (
                    name == '.idea' and
                    os.path.isdir(os.path.join(root_dir, name))
                )
        ]
        if not len(dirs) == 1:
            print("didn't find the idea directory")
            sys.exit(1)
        return dirs[0]


# give directory of project and it finds the idea folder
if len(sys.argv) > 1:
    idea_dir = get_idea_dir(sys.argv[1])


# don't give a directory and it assumes current dir contains idea subdir
if len(sys.argv) == 1:
    idea_dir = get_idea_dir(os.path.dirname(os.path.realpath(__file__)))

# =============================================================================
# Run Configurations
# =============================================================================

install_dir = os.path.join(idea_dir, 'runConfigurations')
config_dir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'runConfigurations')
# make the install directory if it doesn't exist
if not os.path.exists(install_dir):
    os.makedirs(install_dir)
# copy all of the saved configs to the install dir
configs = [
    c for c in os.listdir(config_dir)
    if os.path.isfile(os.path.join(config_dir, c))
]
for config in configs:
    filename = os.path.basename(config)
    install_file = os.path.join(install_dir, filename)
    if not os.path.exists(install_file):
        shutil.copy(
                os.path.join(config_dir, config),
                os.path.join(install_dir, config))

# =============================================================================
# Workspace Defaults
# =============================================================================

# parse the workspace.xml config
workspace_file = "%s/workspace.xml" % (idea_dir)
tree = ET.parse(workspace_file)
root = tree.getroot()

# parse the default ToolWindowManager
tools_config_file = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'tools-config.xml')
default_tools = ET.parse(tools_config_file).getroot()

xtools = 'component[@name="ToolWindowManager"]'
tools = root.find(xtools)
if tools:
    root.remove(tools)
root.append(default_tools)

tree.write(workspace_file)

msg = """
--- updated defaults! ---

NOTE: IntelliJ will overwrite these changes on exit if the project is running.
You will need to close the project window and re-run this program
"""
print(msg)
