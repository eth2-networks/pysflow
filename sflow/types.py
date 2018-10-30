import binascii
import ipaddress


class Base(object):
    @staticmethod
    def decode(unpacker):
        raise NotImplementedError


class BaseStruct(Base):
    @classmethod
    def decode(cls, unpacker):
        data = {}

        for name, decoder in cls.__struct__:
            data[name] = decoder.decode(unpacker)

        return data


class BaseDataFormat(BaseStruct):
    @classmethod
    def get_decoder(cls, data_format):
        for c in cls.__subclasses__():
            if c.__format__ == data_format:
                return c
        raise ValueError('Unknown data format: {}'.format(data_format))


class BaseSampleFormat(BaseDataFormat):
    pass


class BaseCounterData(BaseDataFormat):
    pass


class BaseFlowData(BaseDataFormat):
    pass


class UInt(Base):
    @staticmethod
    def decode(unpacker):
        return unpacker.unpack_uint()


class UHyper(Base):
    @staticmethod
    def decode(unpacker):
        return unpacker.unpack_uhyper()


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


class Address(Base):
    UNKNOWN = 0
    IP_V4 = 1
    IP_V6 = 2

    @staticmethod
    def _decode_ipv4(unpacker):
        address = unpacker.unpack_fopaque(4)

        return '.'.join(map(str, address))

    @staticmethod
    def _decode_ipv6(unpacker):
        address = unpacker.unpack_fopaque(16)

        return str(ipaddress.ip_address(address))

    @classmethod
    def decode(cls, unpacker):
        address_type = unpacker.unpack_uint()

        if address_type == cls.IP_V4:
            return cls._decode_ipv4(unpacker)
        elif address_type == cls.IP_V6:
            return cls._decode_ipv6(unpacker)
        else:
            raise TypeError('Unknown address type: {}'.format(address_type))

        return address_type


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


class FlowRecord(BaseStruct):
    @staticmethod
    def decode(unpacker):
        data_format = DataFormat.decode(unpacker)
        record_length = UInt.decode(unpacker)

        Decoder = BaseFlowData.get_decoder(data_format)
        data = Decoder.decode(unpacker)

        data['data_format'] = data_format
        data['record_length'] = record_length

        return data


class CounterRecord(Base):
    @staticmethod
    def decode(unpacker):
        data_format = DataFormat.decode(unpacker)
        record_length = UInt.decode(unpacker)

        Decoder = BaseCounterData.get_decoder(data_format)
        data = Decoder.decode(unpacker)

        data['data_format'] = data_format
        data['record_length'] = record_length

        return data


class FlowSample(BaseSampleFormat):
    __format__ = (0, 1)
    __struct__ = [
        ('sequence_number', UInt),
        ('source_id', UInt),
        ('sampling_rate', UInt),
        ('sample_pool', UInt),
        ('drops', UInt),
        ('input', UInt),
        ('output', UInt),
        ('flow_records', Array(FlowRecord)),
    ]


class CountersSample(BaseSampleFormat):
    __format__ = (0, 2)
    __struct__ = [
        ('sequence_number', UInt),
        ('source_id', UInt),
        ('counters', Array(CounterRecord)),
    ]


class SampledHeader(BaseFlowData):
    __format__ = (0, 1)
    __struct__ = [
        ('protocol', UInt),
        ('frame_length', UInt),
        ('stripped', UInt),
        ('header', HexOpaque),
    ]


class ExtendedSwitchData(BaseFlowData):
    __format__ = (0, 1001)
    __struct__ = [
        ('src_vlan', UInt),
        ('src_priority', UInt),
        ('dst_vlan', UInt),
        ('dst_priority', UInt),
    ]


class ExtendedRouterData(BaseFlowData):
    __format__ = (0, 1002)
    __struct__ = [
        ('nexthop', Address),
        ('src_mask_len', UInt),
        ('dst_mask_len', UInt),
    ]


class ExtendedGatewayData(BaseFlowData):
    __format__ = (0, 1003)
    __struct__ = [
        ('nexthop', Address),
        ('as', UInt),
        ('src_as', UInt),
        ('src_peer_as', UInt),
        ('dst_as_path', Array(ASPath)),
        ('communities', Array(Community)),
        ('localpref', UInt),
    ]


class IfCounters(BaseCounterData):
    __format__ = (0, 1)
    __struct__ = [
        ('ifIndex', UInt),
        ('ifType', UInt),
        ('ifSpeed', UHyper),
        ('ifDirection', UInt),
        ('ifStatus', UInt),
        ('ifInOctets', UHyper),
        ('ifInUcastPkts', UInt),
        ('ifInMulticastPkts', UInt),
        ('ifInBroadcastPkts', UInt),
        ('ifInDiscards', UInt),
        ('ifInErrors', UInt),
        ('ifInUnknownProtos', UInt),
        ('ifOutOctets', UHyper),
        ('ifOutUcastPkts', UInt),
        ('ifOutMulticastPkts', UInt),
        ('ifOutBroadcastPkts', UInt),
        ('ifOutDiscards', UInt),
        ('ifOutErrors', UInt),
        ('ifPromiscuousMode', UInt),
    ]


class SampleRecord(Base):
    @staticmethod
    def decode(unpacker):
        data_format = DataFormat.decode(unpacker)
        sample_length = UInt.decode(unpacker)

        Decoder = BaseSampleFormat.get_decoder(data_format)
        data = Decoder.decode(unpacker)
        data['data_format'] = data_format
        data['sample_length'] = sample_length

        return data


class Datagram(BaseStruct):
    __struct__ = [
        ('version', UInt),
        ('agent_address', Address),
        ('sub_agent_id', UInt),
        ('sequence_number', UInt),
        ('uptime', UInt),
        ('samples', Array(SampleRecord)),
    ]
