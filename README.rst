pysflow
=======
A simple sFlow parser library for Python.

Requirements
------------
This project is built and tested against Python 3.6 and 3.7. Older versions
might or might not work. Tests for this are planned to be included in later
releases. The library has no external dependencies and only uses the built-in
``xdrlib`` and ``ipaddress`` functions.

Installation
------------
To install the library, run::

    pip install pysflow

or if you have cloned this Git repository, run::

   python setup.py install

Usage
-----

A very simple program that uses the library can be found in ``example.py``.
There is one high-level entry point, ``sflow.decode()``, which takes a byte
array as the argument. It will decode a raw sFlow datagram into a Python dict.
Each component (flow record, data type, etc.) can be used in a stand-alone way
by calling the static ``.decode()`` function on the class. This function takes
an ``xdrlib.Unpacker`` as an argument.
