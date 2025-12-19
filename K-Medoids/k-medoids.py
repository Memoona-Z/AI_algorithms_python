import random

k = 3
# list of k medoid points :
centroids = []   

# all data points from file in list format:       
all_data_points = []   

# grouping of data_points to their nearest medoids:
groups_dict = {}

# Manhattan's Distance:
def find_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# reading data from file and appending in all_data_points list
with open("clustering_data.txt", "r") as f:
    for line in f:
        parts = line.split(",")
        x = float(parts[0])
        y = float(parts[1])
        all_data_points.append([x, y])

n = len(all_data_points)

# initialize k medoids randomly from the datapoints :
centroids = random.sample(all_data_points, k)

# clustering func :
def clustering(medoids):
    # initializing empty lists of "k" groups :
    for i in range(k):
        groups_dict[i] = []
    
    # assign each point to the nearest medoid :
    for pt in all_data_points:
        dists = [find_distance(pt, medoids[m]) for m in range(k)]
        min_idx = dists.index(min(dists))
        groups_dict[min_idx].append(pt)

# func to calculate the total cost of clustering :
def calculate_cost(medoids):
    cost = 0
    for i in range(k):
        for pt in groups_dict[i]:
            cost += find_distance(pt, medoids[i])
    return cost

# func to randomly swap a medoid with a non-medoid point:
def try_random_swap(medoids):
    m_idx = random.randint(0, k-1)
    non_medoids = [pt for pt in all_data_points if pt not in medoids]
    new_candidate = random.choice(non_medoids)
    temp_medoids = medoids.copy()
    temp_medoids[m_idx] = new_candidate
    clustering(temp_medoids)
    new_cost = calculate_cost(temp_medoids)

    return m_idx, new_candidate, new_cost

iteration = 0
# counts how many iterations without improvement:
no_improvement_rounds = 0

clustering(centroids)
prev_cost = calculate_cost(centroids)
max_no_improve = 10

# main loop: keep trying random swaps until no improvement is observed :
while True:
    iteration += 1
    # Random Swap:
    medoid_index, candidate, new_cost = try_random_swap(centroids)

    # if new cost is better, accept the swap: 
    if new_cost < prev_cost:
        centroids[medoid_index] = candidate
        prev_cost = new_cost
        no_improvement_rounds = 0
        print(f"Iteration {iteration}: Improved cost :- {prev_cost}")
    else:
        no_improvement_rounds += 1
    # Stop if no improvement :
    if no_improvement_rounds >= max_no_improve:
        print("\nNo improvement found for many attempts.")
        print("Algorithm has converged!\n")
        break

# Final clustering using the best medoids :
clustering(centroids)

# display each cluster data points:
print("Final Medoids and Clusters:")

for i in range(k):
    print(f"\nMedoid {i}: {centroids[i]}")
    print("Points:")
    for pt in groups_dict[i]:
        print(pt)
