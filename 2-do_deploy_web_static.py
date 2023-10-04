#!/usr/bin/python3
#!/usr/bin/python3

""" Test deploy web static """
from datetime import datetime
from fabric.api import run, env, put, local
from os.path import exists

user = env.user = "ubuntu"
host = env.hosts = ["54.90.63.243", "54.90.4.180"]


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


def do_deploy(archive_path):
    """deploy package to remote server
    Arguments:
        archive_path: path to archive to deploy
    """
    if not archive_path or not exists(archive_path):
        return False
    put(archive_path, '/tmp')
    ar_name = archive_path[archive_path.find("/") + 1: -4]
    try:
        run('mkdir -p /data/web_static/releases/{}/'.format(ar_name))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'.format(
                ar_name, ar_name
        ))
        run('rm /tmp/{}.tgz'.format(ar_name))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(
                ar_name, ar_name
        ))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            ar_name
        ))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ \
            /data/web_static/current'.format(
            ar_name
        ))
        print("New version deployed!")
        return True
    except:
        return False
