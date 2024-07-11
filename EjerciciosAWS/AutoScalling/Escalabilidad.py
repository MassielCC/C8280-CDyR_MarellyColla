class Server:
    def __init__(self, cpu_capacity, memory_capacity):
        self.cpu_capacity = cpu_capacity
        self.memory_capacity = memory_capacity
        self.current_load = 0
    def scale_up(self, additional_cpu, additional_memory):
        self.cpu_capacity += additional_cpu
        self.memory_capacity += additional_memory

#Escalabilidad horizontal
class ServerCluster:
    def __init__(self):
        self.servers = []
    def add_server(self, server):
        self.servers.append(server)
    def remove_server(self):
        if self.servers:
            self.servers.pop()
    def distribute_load(self, load):
        if not self.servers:
            print("No servers available.")
            return
        load_per_server = load / len(self.servers)
        for server in self.servers:
            server.current_load += load_per_server

# Example usage
server1 = Server(cpu_capacity=4, memory_capacity=8)
server2 = Server(cpu_capacity=4, memory_capacity=8)
cluster = ServerCluster()
cluster.add_server(server1)
cluster.add_server(server2)
cluster.distribute_load(10)