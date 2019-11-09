from src.networking.packets import Packet

from src.networking.types import (
    String, Long
)


# Formerly known as state_status_clientbound.
def get_packets(context):
    packets = {
        ResponsePacket,
        PingResponsePacket,
    }
    return packets


class ResponsePacket(Packet):
    id = 0x00
    packet_name = "response"
    definition = [
        {'json_response': String}]


class PingResponsePacket(Packet):
    id = 0x01
    packet_name = "ping"
    definition = [
        {'time': Long}]
