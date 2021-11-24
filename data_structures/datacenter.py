import re
from data_structures.cluster import Cluster


class Datacenter:
    def __init__(self, name, cluster_dict):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """
        self.name = name
        self.clusters = []

        for key, value in cluster_dict.items():
            cluster = Cluster(key, value['networks'], value['security_level'])
            self.clusters.append(cluster)

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """

        cluster_reg = '^' + self.name[:3].upper() + '-[0-9]{1,3}$'
        self.clusters = list(filter(lambda cluster: re.search(cluster_reg, cluster.name), self.clusters))

    def __repr__(self):
        return f"Datacenter = {self.name}\nCluster = {self.clusters}\n"
