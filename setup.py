
import os
from setuptools import setup


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

def readlines(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).readlines()


setup(
    name='pyflo',
    version=0.1,
    author='benjiyamin, see AUTHORS.md',
    author_email='benjiyamin@gmail.com',
    description='PyFlo is an open-source library written in Python for performing hydraulic and '
                'hydrology stormwater analysis. ',
    license='GNU General Public License v3 (GPLv3), see LICENSE.md',
    keywords='hydraulics hydrology storm simulation,',
    url='https://benjiyamin.github.io/pyflo',
    packages=['pyflo'],
    long_description=read('README.md'),
    install_requires = readlines('requirements/production.txt'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python'
    ],
)
