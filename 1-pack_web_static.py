from datetime import datetime
from fabric.api import *


def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static folder
    """

    # Get the current date and time
    time = datetime.now()

    # Define the name of the archive using the current date and time
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'

    # Create the 'versions' folder if it doesn't exist
    local('mkdir -p versions')

    # Create the .tgz archive
    create = local('tar -cvzf versions/{} web_static'.format(archive))

    # Check if the archive was created successfully
    if create is not None:
        return archive
    else:
        return None
