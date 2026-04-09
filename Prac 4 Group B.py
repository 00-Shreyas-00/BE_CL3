import numpy as np

dist = np.array([
    [0, 2, 2, 5],
    [2, 0, 3, 4],
    [2, 3, 0, 1],
    [5, 4, 1, 0]
])

pheromone = np.ones(dist.shape)


def route_length(route):
    return sum(dist[route[i], route[i + 1]] for i in range(len(route) - 1))


best_route = None
best_length = float('inf')

for _ in range(50):
    route = list(np.random.permutation(4))
    length = route_length(route)

    if length < best_length:
        best_length = length
        best_route = route

print("Best Route:", best_route)
print("Distance:", best_length)