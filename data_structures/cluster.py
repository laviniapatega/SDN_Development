from data_structures.network_collection import NetworkCollection


class Cluster:
    def __init__(self, name, network_dict, security_level):
        """
        Constructor for Cluster data structure.

        self.name -> str
        self.security_level -> int
        self.networks -> list(NetworkCollection)
        """
        self.name = name
        self.security_level = security_level
        self.networks = []

        for key, value in network_dict.items():
            network = NetworkCollection(key, value)
            self.networks.append(network)

    def __repr__(self):
        return f"{self.name}\nsecurity_level = {self.security_level}\nnetwork_range = {self.networks}\n"
