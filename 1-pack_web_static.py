#!/usr/bin/python3

from datetime import datetime
from fabric.api import local
from os.path import exists


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: The path to the generated archive
        file, or None if an error occurs.
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(date)
    cmd = "tar -cvzf {} web_static".format(path)
    try:
        if not exists("versions"):
            local("mkdir versions")
        local(cmd)
        return path
    except Exception:
        return None
