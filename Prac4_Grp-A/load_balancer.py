import random
import time

# Server class
class Server:
    def __init__(self, name):
        self.name = name
        self.load = 0  # number of active requests

    def handle_request(self):
        self.load += 1

    def finish_request(self):
        if self.load > 0:
            self.load -= 1

    def __str__(self):
        return f"{self.name} (Load: {self.load})"


# Load Balancer Class
class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0  # for round robin

    # Round Robin
    def round_robin(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server

    # Least Connections
    def least_connections(self):
        return min(self.servers, key=lambda s: s.load)

    # Random Selection
    def random_selection(self):
        return random.choice(self.servers)


# Simulate client requests
def simulate_requests(lb, algorithm, num_requests=10):
    print(f"\n--- Using {algorithm} Algorithm ---")

    for i in range(1, num_requests + 1):
        # Choose algorithm
        if algorithm == "round_robin":
            server = lb.round_robin()
        elif algorithm == "least_connections":
            server = lb.least_connections()
        elif algorithm == "random":
            server = lb.random_selection()

        # Assign request
        server.handle_request()
        print(f"Request {i} -> {server.name}")

        # Simulate completion randomly
        if random.random() < 0.5:
            server.finish_request()

        # Show server loads
        for s in lb.servers:
            print(s, end=" | ")
        print("\n")

        time.sleep(0.5)


# ---------------- MAIN ----------------
if __name__ == "__main__":
    # Create servers
    servers = [Server(f"Server-{i}") for i in range(1, 4)]

    # Create load balancer
    lb = LoadBalancer(servers)

    # Run simulations
    simulate_requests(lb, "round_robin", 8)
    simulate_requests(lb, "least_connections", 8)
    simulate_requests(lb, "random", 8)