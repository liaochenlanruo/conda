import platform
import os

from conda import plugins
from conda.common._os.linux import linux_get_libc_version


@plugins.hookimp
def conda_cli_register_virtual_packages():
    if platform.system != 'Windows':
        return

    yield plugins.CondaVirtualPackage('win', None)
