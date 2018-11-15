from sflow.base import Base, BaseStruct, BaseSampleFormat
from sflow.base import BaseCounterData, BaseFlowData
from sflow.types import Address, Array, DataFormat, UInt


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


class CountersSample(BaseSampleFormat):
    __format__ = (0, 2)
    __struct__ = [
        ('sequence_number', UInt),
        ('source_id', UInt),
        ('counters', Array(CounterRecord)),
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
