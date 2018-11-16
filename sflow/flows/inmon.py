from sflow.base import BaseFlowData
from sflow.types import Array, Int, UInt, String, Opaque
from sflow.types import ASPath, Address, Community, HexOpaque, IPv4, IPv6, MAC


class SampledHeader(BaseFlowData):
    __format__ = (0, 1)
    __struct__ = [
        ('protocol', UInt),
        ('frame_length', UInt),
        ('stripped', UInt),
        ('header', HexOpaque),
    ]


class SampledEthernet(BaseFlowData):
    __format__ = (0, 2)
    __struct__ = [
        ('length', UInt),
        ('src_mac', MAC),
        ('dst_mac', MAC),
        ('type', UInt),
    ]


class SampledIPv4(BaseFlowData):
    __format__ = (0, 3)
    __struct__ = [
        ('length', UInt),
        ('protocol', UInt),
        ('src_ip', IPv4),
        ('dst_ip', IPv4),
        ('src_port', UInt),
        ('dst_port', UInt),
        ('tcp_flags', UInt),
        ('tos', UInt),
    ]


class SampledIPv6(BaseFlowData):
    __format__ = (0, 4)
    __struct__ = [
        ('length', UInt),
        ('protocol', UInt),
        ('src_ip', IPv6),
        ('dst_ip', IPv6),
        ('src_port', UInt),
        ('dst_port', UInt),
        ('tcp_flags', UInt),
        ('priority', UInt),
    ]


class ExtendedSwitch(BaseFlowData):
    __format__ = (0, 1001)
    __struct__ = [
        ('src_vlan', UInt),
        ('src_priority', UInt),
        ('dst_vlan', UInt),
        ('dst_priority', UInt),
    ]


class ExtendedRouter(BaseFlowData):
    __format__ = (0, 1002)
    __struct__ = [
        ('nexthop', Address),
        ('src_mask_len', UInt),
        ('dst_mask_len', UInt),
    ]


class ExtendedGateway(BaseFlowData):
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


class ExtendedUser(BaseFlowData):
    __format__ = (0, 1004)
    __struct__ = [
        ('src_charset', UInt),
        ('src_user', Opaque),
        ('dst_charset', UInt),
        ('dst_user', Opaque),
    ]


class ExtendedURL(BaseFlowData):
    __format__ = (0, 1005)
    __struct__ = [
        ('direction', UInt),
        ('url', String),
        ('host', String),
    ]


class ExtendedMPLS(BaseFlowData):
    __format__ = (0, 1006)
    __struct__ = [
        ('nexthop', Address),
        ('in_stack', Array(Int)),
        ('out_stack', Array(Int)),
    ]


class ExtendedNAT(BaseFlowData):
    __format__ = (0, 1007)
    __struct__ = [
        ('src_address', Address),
        ('dst_address', Address),
    ]


class ExtendedMPLSTunnel(BaseFlowData):
    __format__ = (0, 1008)
    __struct__ = [
        ('tunnel_lsp_name', String),
        ('tunnel_id', UInt),
        ('tunnel_cos', UInt),
    ]


class ExtendedMPLSVC(BaseFlowData):
    __format__ = (0, 1009)
    __struct__ = [
        ('vc_instance_name', String),
        ('vll_vc_id', UInt),
        ('vc_label_cos', UInt),
    ]


class ExtendedMPLSFEC(BaseFlowData):
    __format__ = (0, 1010)
    __struct__ = [
        ('mplsFTNDescr', String),
        ('mplsFTNMask', UInt),
    ]


class ExtendedMPLSLDPFEC(BaseFlowData):
    __format__ = (0, 1011)
    __struct__ = [
        ('mplsFecAddrPrefixLength', UInt),
    ]


class ExtendedVLANTunnel(BaseFlowData):
    __format__ = (0, 1012)
    __struct__ = [
        ('stack', Array(UInt)),
    ]
