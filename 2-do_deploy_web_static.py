#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists

# Define the IP addresses of the web servers
env.hosts = ['54.89.109.87', '100.25.190.21']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers and deploys it
    """

    # Check if the archive_path exists
    if exists(archive_path) is False:
        return False

    try:
        # Extract file name and remove extension
        file_name = archive_path.split("/")[-1]
        no_extension = file_name.split(".")[0]

        # Define the path where the archive will be deployed
        path = "/data/web_static/releases/"

        # Upload the archive to the /tmp/ directory on the server
        put(archive_path, '/tmp/')

        # Create a directory to store the files from the archive
        run('mkdir -p {}{}/'.format(path, no_extension))

        # Extract the archive contents into the deployment directory
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_extension))

        # Remove the uploaded archive from the /tmp/ directory
        run('rm /tmp/{}'.format(file_name))

        # Move the contents of the extracted folder to a new location
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_extension))

        # Remove the original web_static folder
        run('rm -rf {}{}/web_static'.format(path, no_extension))

        # Update the symbolic link to point to the new deployment
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_extension))

        return True
    except Exception as e:
        return False
