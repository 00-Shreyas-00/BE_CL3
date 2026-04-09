import numpy as np
import random

# ---------------- NEURAL NETWORK ----------------
class SimpleNN:
    def __init__(self, weights):
        # weights: [w1, w2, w3, bias]
        self.w = weights

    def predict(self, x):
        # simple linear + sigmoid activation
        z = self.w[0]*x[0] + self.w[1]*x[1] + self.w[2]*x[2] + self.w[3]
        return 1 / (1 + np.exp(-z))


# ---------------- FITNESS FUNCTION ----------------
# Simulated dataset (spray drying parameters)
# Inputs: temperature, pressure, flow_rate
# Output: efficiency (0–1)

data = [
    ([60, 2, 10], 0.7),
    ([70, 3, 12], 0.8),
    ([80, 4, 14], 0.9),
    ([65, 2.5, 11], 0.75),
]

def fitness(weights):
    nn = SimpleNN(weights)
    error = 0
    for x, y in data:
        pred = nn.predict(x)
        error += (y - pred) ** 2
    return -error  # maximize fitness (minimize error)


# ---------------- GENETIC ALGORITHM ----------------
POP_SIZE = 10
GENS = 20
MUTATION_RATE = 0.1

# Initialize population
def init_population():
    return [np.random.uniform(-1, 1, 4) for _ in range(POP_SIZE)]

# Selection (tournament)
def select(pop):
    return max(random.sample(pop, 3), key=fitness)

# Crossover
def crossover(p1, p2):
    point = random.randint(1, 3)
    child = np.concatenate((p1[:point], p2[point:]))
    return child

# Mutation
def mutate(child):
    if random.random() < MUTATION_RATE:
        idx = random.randint(0, 3)
        child[idx] += random.uniform(-0.5, 0.5)
    return child


# ---------------- MAIN ----------------
if __name__ == "__main__":
    population = init_population()

    for gen in range(GENS):
        new_population = []
        for _ in range(POP_SIZE):
            p1 = select(population)
            p2 = select(population)
            child = crossover(p1, p2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

        best = max(population, key=fitness)
        print(f"Generation {gen+1} Best Fitness: {fitness(best):.4f}")

    # Final result
    best_weights = max(population, key=fitness)
    print("\nOptimized Weights:", best_weights)

    # Test prediction
    nn = SimpleNN(best_weights)
    test_input = [75, 3.5, 13]
    print("Predicted Efficiency:", nn.predict(test_input))