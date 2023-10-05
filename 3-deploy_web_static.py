#!/usr/bin/python3
"""pack and deploy content to server
"""
from fabric.api import local, env, run, put
from datetime import datetime
import os

env.hosts = ["54.90.63.243", "54.90.4.180"]

env.user = "ubuntu"


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
        if not os.path.exists("versions"):
            local("mkdir versions")
        local(cmd)
        return path
    except Exception:
        return None


def do_deploy(archive_path):
    """Deploy package to remote server.

    Args:
        archive_path (str): Path to archive to deploy.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    # Check if archive_path is valid
    if not archive_path or not os.path.exists(archive_path):
        return False

    # Copy the archive to /tmp
    put(archive_path, "/tmp")

    # Extract the name of the archive
    ar_name = archive_path[archive_path.find("/") + 1: -4]

    try:
        # Create the necessary release directory
        run("mkdir -p /data/web_static/releases/{}/".format(ar_name))

        # Extract the archive to the release directory
        run(
            "tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".format(
                ar_name, ar_name
            )
        )

        # Remove the archive from /tmp
        run("rm /tmp/{}.tgz".format(ar_name))

        # Move the contents of the web_static folder to the release directory
        run(
            "mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(ar_name, ar_name)
        )

        # Remove the empty web_static folder
        run("rm -rf /data/web_static/releases/{}/web_static".format(ar_name))

        # Remove the current symlink
        run("rm -rf /data/web_static/current")

        # Create a new symlink to the latest release
        run(
            "ln -s /data/web_static/releases/{}/ "
            "/data/web_static/current".format(ar_name)
        )

        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """
    function to pack and deploy
    """
    pack = do_pack()
    if pack:
        return do_deploy(pack)
    return False
