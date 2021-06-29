from setuptools import setup

with open("README.md", "r") as file:
   long_description = file.read()

setup(
	name='wday',
	version='1.0',    
	description='''A simple Data storage language''',
	long_description=long_description,
	long_description_content_type="text/markdown",
	url='https://github.com/Whirlpool-Programmer/wday',
	author='Whirlpool-Programmer',
	author_email='whirlpool.programmer@outlook.com',
	license='MIT License',
	packages=['wday'],
	classifiers =[
	'Programming Language :: Python :: 3',
	'License :: OSI Approved :: MIT License',
	'Operating System :: OS Independent'
	]
	
)
