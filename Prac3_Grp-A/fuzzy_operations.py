# Fuzzy Set Operations & Relations

# Define fuzzy sets as dictionaries
# Example: A = {'x1': 0.2, 'x2': 0.5}

def fuzzy_union(A, B):
    return {x: max(A.get(x, 0), B.get(x, 0)) for x in set(A) | set(B)}

def fuzzy_intersection(A, B):
    return {x: min(A.get(x, 0), B.get(x, 0)) for x in set(A) | set(B)}

def fuzzy_complement(A):
    return {x: 1 - A[x] for x in A}

def fuzzy_difference(A, B):
    return {x: min(A.get(x, 0), 1 - B.get(x, 0)) for x in set(A) | set(B)}

# Cartesian product (fuzzy relation)
def cartesian_product(A, B):
    relation = {}
    for a in A:
        for b in B:
            relation[(a, b)] = min(A[a], B[b])
    return relation

# Max-Min Composition
def max_min_composition(R1, R2):
    result = {}
    X = set([x for (x, _) in R1])
    Z = set([z for (_, z) in R2])

    for x in X:
        for z in Z:
            values = []
            for y in set([y for (_, y) in R1 if _ == x]):
                if (x, y) in R1 and (y, z) in R2:
                    values.append(min(R1[(x, y)], R2[(y, z)]))
            result[(x, z)] = max(values) if values else 0
    return result


# ------------------- MAIN PROGRAM -------------------

if __name__ == "__main__":
    # Define fuzzy sets
    A = {'x1': 0.2, 'x2': 0.5, 'x3': 0.8}
    B = {'x1': 0.6, 'x2': 0.3, 'x4': 0.9}

    print("Fuzzy Set A:", A)
    print("Fuzzy Set B:", B)

    print("\nUnion:", fuzzy_union(A, B))
    print("Intersection:", fuzzy_intersection(A, B))
    print("Complement of A:", fuzzy_complement(A))
    print("Difference A - B:", fuzzy_difference(A, B))

    # Relations
    print("\nCartesian Product (R1 = A x B):")
    R1 = cartesian_product(A, B)
    for k, v in R1.items():
        print(f"{k}: {v}")

    print("\nCartesian Product (R2 = B x A):")
    R2 = cartesian_product(B, A)
    for k, v in R2.items():
        print(f"{k}: {v}")

    # Max-Min Composition
    print("\nMax-Min Composition (R1 o R2):")
    comp = max_min_composition(R1, R2)
    for k, v in comp.items():
        print(f"{k}: {v}")