import random
import math

# Objective function (we try to maximize this)
def fitness(x):
    return math.sin(x) + x * 0.1   # simple function

# Generate initial population
def init_population(size):
    return [random.uniform(0, 10) for _ in range(size)]

# Clone antibodies (better fitness → more clones)
def clone(population):
    clones = []
    for x in population:
        n_clones = int(fitness(x) * 5) if fitness(x) > 0 else 1
        for _ in range(max(1, n_clones)):
            clones.append(x)
    return clones

# Mutation (small variation)
def mutate(clones):
    mutated = []
    for x in clones:
        new_x = x + random.uniform(-0.5, 0.5)
        new_x = max(0, min(10, new_x))  # keep within bounds
        mutated.append(new_x)
    return mutated

# Selection (choose best individuals)
def select(population, size):
    return sorted(population, key=fitness, reverse=True)[:size]


# ---------------- MAIN ----------------
if __name__ == "__main__":
    POP_SIZE = 10
    GENERATIONS = 20

    # Step 1: Initialize population
    population = init_population(POP_SIZE)

    for gen in range(GENERATIONS):
        # Step 2: Clone
        clones = clone(population)

        # Step 3: Mutate clones
        mutated = mutate(clones)

        # Step 4: Select best individuals
        population = select(mutated, POP_SIZE)

        best = population[0]
        print(f"Generation {gen+1}: Best x = {best:.4f}, Fitness = {fitness(best):.4f}")

    print("\nFinal Best Solution:")
    print(f"x = {population[0]:.4f}, Fitness = {fitness(population[0]):.4f}")