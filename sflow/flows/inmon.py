from sflow.base import BaseFlowData
from sflow.types import ASPath, Address, Array, Community, HexOpaque, UInt


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
