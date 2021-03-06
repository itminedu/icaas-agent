#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 GRNET S.A.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import icaas_agent

from setuptools import setup, find_packages

setup(
    name='icaas-agent',
    version=icaas_agent.__version__,
    description='Image Creator as a Service agent',
    long_description=open('README.md').read(),
    url='https://github.com/grnet/icaas',
    download_url='https://pypi.python.org/pypi/icaas-agent',
    author='Synnefo development team',
    author_email='synnefo-devel@googlegroups.com',
    maintainer='Synnefo development team',
    maintainer_email='synnefo-devel@googlegroups.com',
    license='GNU GPLv3',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['kamaki>=0.9', 'requests', 'python-daemon'],
    entry_points={
        'console_scripts': [
                'icaas = icaas_agent.monitord:main']
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Console :: Curses',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7'],
    keywords='cloud IaaS OS images'
)
# vim: set sta sts=4 shiftwidth=4 sw=4 et ai :
