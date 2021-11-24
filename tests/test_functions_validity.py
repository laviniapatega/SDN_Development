import unittest
import ipaddress
from data_structures.datacenter import Datacenter


class FunctionsValidity(unittest.TestCase):
    """
            Unit tests:
            test_remove_cluster()
            test_ip_validity()
            test_valid_sorting()
    """
    def setUp(self):
        data = {'Romania': {'Rom-123': {'security_level': 1, 'networks': {
            '192.168.0.0/24': [{'address': '255.255.255.0', 'available': True, 'last_used': '30/01/20 17:00:00'},
                               {'address': '192.168..0.3', 'available': True, 'last_used': '30/01/20 17:00:00'}]}},
                            'ROM-1234': {'security_level': 1, 'networks': {'192.168.0.0/24': [
                                {'address': '192.168.0.a', 'available': True, 'last_used': '30/01/20 17:00:00'},
                                {'address': '192.168.0', 'available': True, 'last_used': '30/01/20 17:00:00'}]}},
                            'ROM123-': {'security_level': 1, 'networks': {'192.168.0.0/24': [
                                {'address': '999.256.3.0', 'available': True, 'last_used': '30/01/20 17:00:00'},
                                {'address': 'ipaddress', 'available': True, 'last_used': '30/01/20 17:00:00'}]}},
                            'ROM-123': {'security_level': 1, 'networks': {'192.168.0.0/24': [
                                {'address': '192.168.0.2', 'available': True, 'last_used': '30/01/20 17:00:00'},
                                {'address': '192.168.0.123', 'available': True, 'last_used': '30/01/20 17:00:00'},
                                {'address': '192.168.0.1', 'available': True, 'last_used': '30/01/20 17:00:00'}]}}}}

        self.datacenters = [
            Datacenter(key, value)
            for key, value in data.items()
        ]

    def test_remove_cluster(self):
        """
        Check the remove_invalid_clusters method removes invalid records from the cluster list.
        """

        for datacenter in self.datacenters:
            datacenter.remove_invalid_clusters()

        # Check if the method removes clusters which don't have first three uppercase letters of the Datacenter
        self.assertNotIn('Rom-123', str(self.datacenters), 'Test case failed, removing invalid clusters failed')

        # Check if the method removes clusters which don't have a number of at least one and maximum three digits
        self.assertNotIn('ROM-1234', str(self.datacenters), 'Test case failed, removing invalid clusters failed')

        # Check if the method removes clusters which don't have the dash in the correct position
        self.assertNotIn('ROM123-', str(self.datacenters), 'Test case failed, removing invalid clusters failed')

        # Check if the method keeps a correct named cluster
        self.assertIn('ROM-123', str(self.datacenters), 'Test case failed, keeping valid clusters failed')

    def test_ip_validity(self):
        """
        Check the remove_invalid_records method removes invalid records from the entries list.
        """

        for datacenter in self.datacenters:
            for cluster in datacenter.clusters:
                for network in cluster.networks:
                    network.remove_invalid_records()

        # Check if the method removes invalid entries
        # The address doesn't belong to the IPv4 network of the parent NetworkCollection object -'192.168.0.0/24'
        self.assertNotIn('255.255.255.0', str(self.datacenters), 'Test case failed, removing invalid ip address failed')

        # Check if the method removes invalid entries, if the field is a valid IPv4 address
        self.assertNotIn('192.168..0.3', str(self.datacenters),
                         'Test case failed, removing 192.168..0.3 invalid ip address failed')
        self.assertNotIn('192.168.0.a', str(self.datacenters),
                         'Test case failed, removing 192.168.0.a invalid ip address failed')
        self.assertNotIn('192.168.0$', str(self.datacenters),
                         'Test case failed, removing 192.168.0 invalid ip address failed')
        self.assertNotIn('999.256.3.0', str(self.datacenters),
                         'Test case failed, removing 999.256.3.0 invalid ip address failed')
        self.assertNotIn('ipaddress', str(self.datacenters),
                         'Test case failed, removing ipaddress invalid ip address failed')

        # Check if the method keeps a correct IPv4 address
        self.assertIn('192.168.0.1', str(self.datacenters),
                      'Test case failed, keeping valid 192.168.0.1 ip address failed')

    def test_valid_sorting(self):
        """
        Check the sort_records method sorts correctly the entries.
        """
        # Sorting entries in list in ascending order
        for datacenter in self.datacenters:
            for cluster in datacenter.clusters:
                for network in cluster.networks:
                    network.remove_invalid_records()
                    network.sort_records()

        # Creating a new list address_list with the sorted elements in order
        address_list = []
        for i in range(len(self.datacenters)):
            datacenter = self.datacenters[0]
            for cluster in datacenter.clusters:
                for network in cluster.networks:
                    for entry in network.entries:
                        address_list.append(entry.address)

        # returns True if address_list is correctly sorted, else returns False
        sort_entries = all(ipaddress.IPv4Address(address_list[i]) <= ipaddress.IPv4Address(address_list[i + 1]) for i in
                           range(len(address_list) - 1))
        # Test passes if the list is sorted correctly
        self.assertEqual(sort_entries, True, f'Test case failed, sorting entries failed {address_list}')


if __name__ == '__main__':
    unittest.main()
