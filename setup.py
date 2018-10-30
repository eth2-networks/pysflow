from distutils.core import setup
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='pysflow',
    version='0.0.1dev',
    license='BSD 3-clause "New" or "Revised License"',

    packages=['sflow',],
    include_package_data=True,

    author="Martijn Reening",
    author_email="martijn@reening.net",

    description="sFlow parser, written in Python",
    long_description=long_description,
    long_description_content_type='text/markdown',
)
