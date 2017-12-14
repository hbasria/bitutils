#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md') as fp:
    long_description = fp.read()

setup(
    name='bitutils',
    version='0.1.1',
    description='Crypto Currency utility library',
    long_description=long_description,
    author='Hasan Basri',
    author_email='hbasria@gmail.com',
    license='MIT',
    keywords='Crypto Currency Utility',
    url='https://github.com/hbasria/bitutils',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    test_suite='tests'
)
