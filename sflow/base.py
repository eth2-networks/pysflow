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
