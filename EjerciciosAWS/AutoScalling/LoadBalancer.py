class LoadBalancer:
    def __init__(self):
        self.servers = []
    def add_server(self, server):
        self.servers.append(server)
    def distribute_http_requests(self, requests):
        print("Distributing HTTP requests...")
        for i, request in enumerate(requests):
            server = self.servers[i % len(self.servers)]
            server.handle_request(request)
    def distribute_tcp_requests(self, requests):
        print("Distributing TCP requests...")
        for i, request in enumerate(requests):
            server = self.servers[i % len(self.servers)]
            server.handle_request(request)

class Server:
    def __init__(self, name):
        self.name = name
    def handle_request(self, request):
        print(f"Server {self.name} handling request: {request}")
# Example usage
server1 = Server("Server 1")
server2 = Server("Server 2")
load_balancer = LoadBalancer()
load_balancer.add_server(server1)
load_balancer.add_server(server2)
load_balancer.distribute_http_requests(["Request 1", "Request 2", "Request 3"])
load_balancer.distribute_tcp_requests(["TCP Request 1", "TCP Request 2"])