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

workspace_file = "%s/workspace.xml" % (idea_dir)
tree = ET.parse(workspace_file)

# get all the window info objects and set the auto_hide attr to true
xpath = 'component[@name="ToolWindowManager"]/layout/window_info'
window_infos = tree.getroot().findall(xpath)
for info in window_infos:
    info.set("auto_hide", 'true')

tree.write(workspace_file)

print("updated defaults")
