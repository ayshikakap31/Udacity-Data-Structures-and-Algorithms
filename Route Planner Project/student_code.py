import math
import heapq
def heuristic(start, goal):
    dist = math.sqrt((start[0]-goal[0])**2 + (start[1]-goal[1])**2)
    return dist
def shortest_path(M, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {node: float('inf') for node in M.intersections}
    g_score[start] = 0
    f_score = {node: float('inf') for node in M.intersections}
    f_score[start] = heuristic(M.intersections[start], M.intersections[goal])
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            return reconstruct_path(came_from, current)
        for neighbor in M.roads[current]:
            cost = heuristic(M.intersections[current], M.intersections[neighbor])
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(M.intersections[neighbor], M.intersections[goal])
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    #print("shortest path called")
    return

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()
    return total_path
    