import xdrlib

import sflow.datagram

# Make sure all counter and flow types are registered
import sflow.counters  # noqa
import sflow.flows  # noqa


def decode(data):
    """Decode a bytes object as an sFlow datagram"""

    unpacker = xdrlib.Unpacker(data)
    datagram = sflow.datagram.Datagram.decode(unpacker)

    return datagram
