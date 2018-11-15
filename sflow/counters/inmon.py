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
