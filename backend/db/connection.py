from cassandra.cluster import Cluster

cluster = Cluster(["127.0.0.1"])
session = cluster.connect("cinema")
