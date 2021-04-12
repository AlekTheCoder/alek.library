from setuptools import setup

DISTNAME = 'alek'

VERSION = '0.1.0'

DESCRIPTION = "Alek Chase's personal python library"

LONG_DESCRIPTION = """
**alek** is a python library that contains useful 
functions for Alek Chase
Available functions:
* Hello
* Delay Print
* Clear
* Get int will be working soon... **
Report any bugs or email us with questions: no-reply@gmail.com
"""

LICENSE = 'MIT'

AUTHOR = "Alek Chase"

EMAIL = 'no-reply@gmail.com'

URL = 'https://github.com/AlekTheCoder/alek'

KEYWORDS = ['alek']

REQUIREMENTS = []

PYTHON = ">=3.5"

setup(name=DISTNAME,
      packages=['alek'],
      package_dir={'alek': 'module/alek'},
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type='text/markdown',
      license=LICENSE,
      author=AUTHOR,
      author_email=EMAIL,
      url=URL,
      keywords=KEYWORDS,
      install_requires=REQUIREMENTS,
      python_requires=PYTHON,
      )