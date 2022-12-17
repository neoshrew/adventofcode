from functools import total_ordering
import json


INPUT_FNAME = "input.txt"
# INPUT_FNAME = "test_1.txt"


@total_ordering
class Packet(object):
    def __init__(self, packet):
        self.packet = packet

    def __eq__(self, other):
        return self.packet == other.packet
        

    def __lt__(self, other):
        return self.cmp(self.packet, other.packet)

    @staticmethod
    def cmp(a, b):
        a_is_list = isinstance(a, list)
        b_is_list = isinstance(b, list)
        
        if not a_is_list and not b_is_list:
            return a < b

        if a_is_list and not b_is_list:
            b = [b]
        elif b_is_list and not a_is_list:
            a = [a]

        for a_item, b_item in zip(a, b):
            result = Packet.cmp(a_item, b_item)
            if result is not None:
                return result

        return len(a) < len(b)

    def __str__(self):
        return str(self.packet)


def main():
    divider_packets = [
        Packet([[2]]),
        Packet([[6]]),
    ]
    packets = divider_packets[::]
    with open(INPUT_FNAME) as fandle:
        for line in fandle:
            line = line.strip()
            if line:
                packets.append(Packet(json.loads(line)))

    packets.sort()

    total = 1
    for i, packet in enumerate(packets, 1):
        if packet in divider_packets:
            total *= i
    print(total)
        




if __name__ == "__main__":
    main()