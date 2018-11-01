from distutils.core import setup
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='pysflow',
    url='https://github.com/reening/pysflow',
    version='0.0.2',
    license='BSD 3-clause "New" or "Revised License"',

    packages=['sflow', ],
    include_package_data=True,

    author="Martijn Reening",
    author_email="martijn@reening.net",

    description="sFlow parser, written in Python",
    long_description=long_description,
    long_description_content_type='text/markdown',

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Networking :: Monitoring',
      ]
)
