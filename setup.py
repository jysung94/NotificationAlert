# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='NotificationAlert',
    version='0.1.0',
    description='Notify real time stock price fluctuations',
    long_description=readme,
    author='Joo Sung',
    author_email='irondrum94@gmail.com',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

