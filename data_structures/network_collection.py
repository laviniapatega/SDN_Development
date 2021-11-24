import re
import ipaddress
from data_structures.entry import Entry


class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """
        self.ipv4_network = ipv4_network
        self.entries = []

        for raw_entry in raw_entry_list:
            entry = Entry(raw_entry['address'], raw_entry['available'], raw_entry['last_used'])
            self.entries.append(entry)

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """

        ip_address_reg = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

        self.entries = list(filter(lambda entry: re.search(ip_address_reg, entry.address)
                                   and self.ip_in_range(entry.address), self.entries))

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)

    def ip_in_range(self, ip_address):

        return ipaddress.IPv4Address(ip_address) in ipaddress.IPv4Network(self.ipv4_network)

    def __repr__(self):
        return f"{self.ipv4_network}\n{self.entries}\n"
