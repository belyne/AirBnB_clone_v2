#!/usr/bin/env python3
# Fabric script to generate a .tgz archive

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    try:
        local("mkdir -p versions")
        now = datetime.now()
        date_format = now.strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(date_format)
        local("tar -cvzf {} web_static".format(archive_name))
        
        # Check if the archive was created successfully
        if os.path.exists(archive_name):
            return archive_name
        else:
            return None
    except Exception as e:
        print(e)
        return None
