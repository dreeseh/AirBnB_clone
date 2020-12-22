#!/usr/bin/python3
"""
module that contains the function deploy
"""
from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir


env.hosts = ['34.75.177.144', '35.231.63.237']


def do_pack():
    """
    generates a .tgz archive from the contents of a folder
    """
    try:
        date_time = datetime.now().srtftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        filename = "web_static_{}.tgz".format(date_time)
        local("tar -cvzf versions/{} ".format(filename))
        return filename
    except:
        return None


def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    """
    if not path.isfile(archive_path):
        return False

    file_archive = archive_path.split('/')[1]
    file_no_ext = archive_file.split('.')[0]
    releases = '/data/web_static/releases/{}/'.format(file_no_ext)

    try:
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(releases))
        run('tar -xzf /tmp/{} -C {}'.format(file_archive, releases))
        run('rm /tmp/{}'.format(file_archive))
        run('mv {}/web_static/* {}'.format(releases, releases))
        run('rm -rf {}/web_static'.format(releases))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(releases))
        return True
    except Exception as e:
        return False


def deploy():
    """
    creates and distributes an archive to your web servers
    """
    archive_path = do_pack()
    if archive_path = None:
        return False
    return do_deploy(archive_path)
