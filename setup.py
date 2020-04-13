""" Script for building the cdtz package. """

from setuptools import setup

try:
    import pypandoc

    LONG_DESCRIPTION = pypandoc.convert('README.md', 'rst')
except (ImportError, OSError):
    # OSError is raised when pandoc is not installed.
    LONG_DESCRIPTION = ('cdtz is microservice intended to '
                        'gets the current time zones '
                        'to display them on the client.')

with open('requirements.txt') as outfile:
    REQUIREMENTS_LIST = outfile.read().splitlines()

setup(name='cdtz',
      version='0.1',
      description='cdtz package',
      long_description=LONG_DESCRIPTION,
      url='https://github.com/IrovoyVlad/cusdeb-tz',
      author='Vladislav Yarovoy',
      author_email='vlad_yarovoy_97@mail.ru',
      maintainer='Vladislav Yarovoy',
      maintainer_email='Vladislav Yarovoy vlad_yarovoy_97@mail.ru',
      license='http://www.apache.org/licenses/LICENSE-2.0',
      scripts=['bin/server.py'],
      packages=['cdtz'],
      include_package_data=True,
      data_files=[
          ('', ['requirements.txt',
                'LICENSE'])
      ],
      install_requires=REQUIREMENTS_LIST)
