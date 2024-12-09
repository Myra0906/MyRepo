import random
import time
from collections import deque

VERTICES = 500  # Number of vertices in the graph

# Function to check if an edge exists
def has_edge(edge_list, source, target):
    return any((edge[0] == source and edge[1] == target) or 
               (edge[0] == target and edge[1] == source) for edge in edge_list)

# BFS algorithm
def bfs(edge_list, start):
    if start < 0 or start >= VERTICES:
        raise ValueError("Эхлэх орой (start) нь 0 болон VERTICES-1-ийн хооронд байх ёстой.")
    visited = [False] * VERTICES
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()
        for edge in edge_list:
            neighbor = -1
            if edge[0] == current:
                neighbor = edge[1]
            elif edge[1] == current:
                neighbor = edge[0]
            
            if neighbor != -1 and not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

# Measure BFS runtime
def measure_bfs(edge_list):
    try:
        start_time = time.time()
        bfs(edge_list, 0)
        end_time = time.time()
        return end_time - start_time
    except ValueError as e:
        print(f"Алдаа: {e}")
        return None

# DFS algorithm
def dfs(edge_list, current, visited):
    if current < 0 or current >= VERTICES:
        raise ValueError("Орой (current) нь 0 болон VERTICES-1-ийн хооронд байх ёстой.")
    visited[current] = True
    for edge in edge_list:
        neighbor = -1
        if edge[0] == current:
            neighbor = edge[1]
        elif edge[1] == current:
            neighbor = edge[0]
        
        if neighbor != -1 and not visited[neighbor]:
            dfs(edge_list, neighbor, visited)

# Measure DFS runtime
def measure_dfs(edge_list):
    try:
        start_time = time.time()
        visited = [False] * VERTICES
        dfs(edge_list, 0, visited)
        end_time = time.time()
        return end_time - start_time
    except ValueError as e:
        print(f"Алдаа: {e}")
        return None

# Print edges in the graph
def print_edge_list(edge_list):
    for edge in edge_list:
        print(f"{edge[0]} - {edge[1]}")

# Main function
if __name__ == "__main__":
    try:
        overall_start_time = time.time()

        # Generate the graph
        edge_list = []
        random.seed(42)  # Set seed for reproducibility

        for i in range(VERTICES):
            degree = random.randint(1, 10)  # Random degree between 1 and 10
            for _ in range(degree):
                neighbor = random.randint(0, VERTICES - 1)
                if i != neighbor and not has_edge(edge_list, i, neighbor):
                    edge_list.append((i, neighbor))

        print("Ирмэгийн жагсаалт:")
        print_edge_list(edge_list)

        print("\nЦагийн үр дүн:")
        bfs_time = measure_bfs(edge_list)
        if bfs_time is not None:
            print(f"BFS гүйцэтгэх хугацаа: {bfs_time:.6f} seconds")
        dfs_time = measure_dfs(edge_list)
        if dfs_time is not None:
            print(f"DFS гүйцэтгэх хугацаа: {dfs_time:.6f} seconds")

        overall_end_time = time.time()
        print(f"Програмын нийт ажиллах хугацаа: {overall_end_time - overall_start_time:.6f} seconds")
    except Exception as e:
        print(f"Тодорхойгүй алдаа гарлаа: {e}")