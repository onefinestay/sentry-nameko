from distutils.core import setup
from setuptools import find_packages

setup(
    name='sentry-nameko',
    version='0.1.1',
    packages=find_packages(exclude=['test', 'test.*']),
    url='http://github.com/onefinestay/sentry-nameko',
    author='onefinestay',
    author_email='engineering@onefinestay.com',
    description='Integration helpers for Sentry and Nameko',
    requires=['sentry'],
    entry_points={
        'sentry.apps': [
            'pluginname = sentry_nameko',
        ]
    },
    license='Apache License, Version 2.0',
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ]
)
