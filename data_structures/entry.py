import ipaddress


class Entry:
    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """
        self.address = address
        self.available = available
        self.last_used = last_used

    def __lt__(self, other):

        return ipaddress.IPv4Address(self.address) < ipaddress.IPv4Address(other.address)

    def __repr__(self):
        return f"[address = {self.address}, available = {self.available}, last_used = {self.last_used}]\n"
