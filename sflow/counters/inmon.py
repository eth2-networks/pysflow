from sflow.base import BaseCounterData
from sflow.types import UInt, UHyper


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


class EthernetCounters(BaseCounterData):
    __format__ = (0, 2)
    __struct__ = [
        ('dot3StatsAlignmentErrors', UInt),
        ('dot3StatsFCSErrors', UInt),
        ('dot3StatsSingleCollisionFrames', UInt),
        ('dot3StatsMultipleCollisionFrames', UInt),
        ('dot3StatsSQETestErrors', UInt),
        ('dot3StatsDeferredTransmissions', UInt),
        ('dot3StatsLateCollisions', UInt),
        ('dot3StatsExcessiveCollisions', UInt),
        ('dot3StatsInternalMacTransmitErrors', UInt),
        ('dot3StatsCarrierSenseErrors', UInt),
        ('dot3StatsFrameTooLongs', UInt),
        ('dot3StatsInternalMacReceiveErrors', UInt),
        ('dot3StatsSymbolErrors', UInt),
    ]


class TokenRingCounters(BaseCounterData):
    __format__ = (0, 3)
    __struct__ = [
        ('dot5StatsLineErrors', UInt),
        ('dot5StatsBurstErrors', UInt),
        ('dot5StatsACErrors', UInt),
        ('dot5StatsAbortTransErrors', UInt),
        ('dot5StatsInternalErrors', UInt),
        ('dot5StatsLostFrameErrors', UInt),
        ('dot5StatsReceiveCongestions', UInt),
        ('dot5StatsFrameCopiedErrors', UInt),
        ('dot5StatsTokenErrors', UInt),
        ('dot5StatsSoftErrors', UInt),
        ('dot5StatsHardErrors', UInt),
        ('dot5StatsSignalLoss', UInt),
        ('dot5StatsTransmitBeacons', UInt),
        ('dot5StatsRecoverys', UInt),
        ('dot5StatsLobeWires', UInt),
        ('dot5StatsRemoves', UInt),
        ('dot5StatsSingles', UInt),
        ('dot5StatsFreqErrors', UInt),
    ]


class BaseVGCounters(BaseCounterData):
    __format__ = (0, 4)
    __struct__ = [
        ('dot12InHighPriorityFrames', UInt),
        ('dot12InHighPriorityOctets', UHyper),
        ('dot12InNormPriorityFrames', UInt),
        ('dot12InNormPriorityOctets', UHyper),
        ('dot12InIPMErrors', UInt),
        ('dot12InOversizeFrameErrors', UInt),
        ('dot12InDataErrors', UInt),
        ('dot12InNullAddressedFrames', UInt),
        ('dot12OutHighPriorityFrames', UInt),
        ('dot12OutHighPriorityOctets', UHyper),
        ('dot12TransitionIntoTrainings', UInt),
        ('dot12HCInHighPriorityOctets', UHyper),
        ('dot12HCInNormPriorityOctets', UHyper),
        ('dot12HCOutHighPriorityOctets', UHyper),
    ]


class VLANCounters(BaseCounterData):
    __format__ = (0, 5)
    __struct__ = [
        ('vlan_id', UInt),
        ('octets', UHyper),
        ('ucastPkts', UInt),
        ('multicastPkts', UInt),
        ('broadcastPkts', UInt),
        ('discards', UInt),
    ]


class Processor(BaseCounterData):
    __format__ = (0, 1001)
    __struct__ = [
        ('percentage 5s_cpu', UInt),
        ('percentage 1m_cpu', UInt),
        ('percentage 5m_cpu', UInt),
        ('total_memory', UHyper),
        ('free_memory', UHyper),
    ]
