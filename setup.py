from distutils.core import setup
from setuptools import setup

setup(
	name='event-bus',
	version='1.0.4',
	packages=['event_bus'],
	url='https://github.com/summer-wu/event-bus',
	license='MIT',
	author='Sean Parsons',
	author_email='seanpatrick2013@gmail.com',
	description='A simple python event bus.',
	download_url='https://github.com/seanpar203/event-bus/archive/1.0.2.tar.gz',
)

# python3 setup.py bdist_wheel
#  pip3.7 install dist/event_bus-1.0.4-py3-none-any.whl