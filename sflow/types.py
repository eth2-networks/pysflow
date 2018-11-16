import binascii
import ipaddress

from sflow.base import Base, BaseStruct


class Int(Base):
    @staticmethod
    def decode(unpacker):
        return unpacker.unpack_int()


class UInt(Base):
    @staticmethod
    def decode(unpacker):
        return unpacker.unpack_uint()


class UHyper(Base):
    @staticmethod
    def decode(unpacker):
        return unpacker.unpack_uhyper()


class String(Base):
    @staticmethod
    def decode(unpacker):
        return unpacker.unpack_string()


class Opaque(Base):
    @staticmethod
    def decode(unpacker):
        return unpacker.unpack_opaque()


class HexOpaque(Base):
    @staticmethod
    def decode(unpacker):
        data = unpacker.unpack_opaque()
        return binascii.hexlify(data).decode('utf8')


class Array(object):
    def __init__(self, t):
        self._type = t

    def _decode_item(self, unpacker):
        return self._type.decode(unpacker)

    def decode(self, unpacker):
        return unpacker.unpack_array(lambda: self._decode_item(unpacker))


class IPv4(Base):
    @staticmethod
    def decode(unpacker):
        address = unpacker.unpack_fopaque(4)

        return '.'.join(map(str, address))


class IPv6(Base):
    @staticmethod
    def decode(unpacker):
        address = unpacker.unpack_fopaque(16)

        return str(ipaddress.ip_address(address))


class Address(Base):
    UNKNOWN = 0
    IP_V4 = 1
    IP_V6 = 2

    @classmethod
    def decode(cls, unpacker):
        address_type = unpacker.unpack_uint()

        if address_type == cls.IP_V4:
            return IPv4.decode(unpacker)
        elif address_type == cls.IP_V6:
            return IPv6.decode(unpacker)
        else:
            raise TypeError('Unknown address type: {}'.format(address_type))

        return address_type


class MAC(Base):
    @staticmethod
    def decode(unpacker):
        address = unpacker.unpack_fopaque(6)

        return '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(*address)


class ASPath(BaseStruct):
    __struct__ = [
        ('as_path_type', UInt),
        ('as_path', Array(UInt)),
    ]


class Community(Base):
    @staticmethod
    def decode(unpacker):
        value = UInt.decode(unpacker)
        asn = (value & 0xFFFF0000) >> 16
        community = (value & 0x0000FFFF)

        return (asn, community)


class DataFormat(Base):
    @staticmethod
    def decode(unpacker):
        value = unpacker.unpack_uint()
        enterprise = (value & 0xFFFFF000) >> 12
        data_type = (value & 0x00000FFF)

        return (enterprise, data_type)
