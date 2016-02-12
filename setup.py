#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

def main():
    extra={}

    setup(
        name='TracWikiTabsPlugin',
        version='0.1.1',
        description='Wiki processor to provide tab panels within Trac wiki page',
        license='BSD',  # the same as Trac
        url='http://trac-hacks.org/wiki/TracWikiTabsPlugin',
        author='Jun Omae',
        author_email='jun66j5@gmail.com',
        install_requires=['Trac'],
        packages=find_packages(exclude=['*.tests*']),
        entry_points={
            'trac.plugins': [
                'tracwikitabs.api = tracwikitabs.api',
                'tracwikitabs.macros = tracwikitabs.macros',
            ],
        },
        **extra)

if __name__ == '__main__':
    main()
