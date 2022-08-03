from setuptools import setup

import versioneer

if __name__ == "__main__":
    # Freeze to support parallel compilation when using spawn instead of fork
    setup(
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
    )
