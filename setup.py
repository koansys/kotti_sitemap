import os
import sys
from setuptools import setup, find_packages

VERSION = __import__('kotti_sitemap').__version__

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.md')).read()
except IOError:
    README = ''
try:
    CHANGES = open(os.path.join(here, 'CHANGES.md')).read()
except IOError:
    CHANGES = ''


if sys.argv[-1] == 'publish':  # upload to pypi
    os.system("python setup.py register sdist upload")
    print "You probably want to also tag the version now:"
    print "  git tag -a %s -m 'version %s'" % (VERSION, VERSION)
    print "  git push --tags"
    sys.exit()

setup(
    name='kotti-sitemap',
    version=VERSION,
    license='MIT License',

    install_requires=[
        'kotti',
    ],

    description='Kotti-Sitemap - an addon to easily create a sitemap for your Kotti project.',
    long_description='\n\n'.join([README, CHANGES]),
    keywords='kotti cms pyramid sitemap sqlalchemy',

    author='Josh Finnie',
    author_email='josh@koansys.com',

    url='https://github.com/joshfinnie/kotti-sitemap',

    packages=find_packages(),
    include_package_data=True,

    zip_safe=False,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Pyramid',
    ]
)
