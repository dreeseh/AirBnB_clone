#!/usr/bin/python3
"""
module that contains the do_deploy prototype
"""
from os import path
from fabric.api import env, run, put, local

env.hosts = ['34.75.177.144', '35.231.63.237']
env.user = 'ubuntu'


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
