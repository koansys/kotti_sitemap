import os
import sys
from setuptools import setup, find_packages

VERSION = '0.1a7'

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.txt')).read()
except IOError:
    README = ''
try:
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    CHANGES = ''


if sys.argv[-1] == 'publish':  # upload to pypi
    os.system("python setup.py register sdist upload")
    print "You probably want to also tag the version now:"
    print "  git tag -a %s -m 'version %s'" % (VERSION, VERSION)
    print "  git push --tags"
    sys.exit()

setup(
    name='kotti_sitemap',
    version=VERSION,
    license='http://koansys.com/license.txt',

    install_requires=[
        'kotti',
    ],

    description='Kotti Sitemap - an addon to easily create a sitemap for your Kotti project.',
    long_description='\n\n'.join([README, CHANGES]),
    keywords='kotti cms pyramid sitemap sqlalchemy',

    author='Koansys, LLC',
    author_email='info@koansys.com',

    url='https://github.com/koansys/kotti_sitemap',

    packages=find_packages(),
    include_package_data=True,

    zip_safe=False,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Pyramid',
    ]
)
