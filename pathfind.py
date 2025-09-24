import heapq
import math
from vectors import Vector2i

def astar(
    start: Vector2i,
    goal: Vector2i,
    width: int,
    height: int,
    blocked: set[Vector2i]
) -> list[Vector2i] | None:
    """
    A* on an 8-connected grid with diagonal cost sqrt(2).
    Diagonal moves are disallowed if they would "cut a corner":
    i.e., if either of the two orthogonal tiles along the diagonal is blocked.
    """

    directions: list[tuple[int, int]] = [
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]

    def in_bounds(x: int, y: int) -> bool:
        return 0 <= x < width and 0 <= y < height

    def is_blocked(x: int, y: int) -> bool:
        return (not in_bounds(x, y)) or (Vector2i(x, y) in blocked)

    def can_move(current: Vector2i, dx: int, dy: int) -> bool:
        # Disallow corner cutting for diagonals:
        # moving from (x,y) to (x+dx,y+dy) requires both (x+dx,y) and (x,y+dy) to be free.
        if dx != 0 and dy != 0:
            side_a_x, side_a_y = current.x + dx, current.y
            side_b_x, side_b_y = current.x, current.y + dy
            if is_blocked(side_a_x, side_a_y) or is_blocked(side_b_x, side_b_y):
                return False
        # Also require destination to be free.
        nx, ny = current.x + dx, current.y + dy
        return in_bounds(nx, ny) and (Vector2i(nx, ny) not in blocked)

    def move_cost(dx: int, dy: int) -> float:
        return math.sqrt(2) if dx != 0 and dy != 0 else 1.0

    def heuristic(a: Vector2i, b: Vector2i) -> float:
        # Octile distance (admissible and consistent for 8-connected grids)
        dx, dy = abs(a.x - b.x), abs(a.y - b.y)
        return (dx + dy) + (math.sqrt(2) - 2) * min(dx, dy)

    # Priority queue with a tie-breaker counter to avoid comparing Vector2i
    open_set: list[tuple[float, int, Vector2i]] = []
    counter: int = 0
    heapq.heappush(open_set, (0.0, counter, start))
    counter += 1

    came_from: dict[Vector2i, Vector2i] = {}
    g_score: dict[Vector2i, float] = {start: 0.0}

    while open_set:
        _, _, current = heapq.heappop(open_set)

        if current == goal:
            path: list["Vector2i"] = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for dx, dy in directions:
            if not can_move(current, dx, dy):
                continue

            nx, ny = current.x + dx, current.y + dy
            neighbor = Vector2i(nx, ny)

            tentative_g = g_score[current] + move_cost(dx, dy)
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, counter, neighbor))
                counter += 1
                came_from[neighbor] = current

    return None

if __name__ == "__main__":
    start = Vector2i(0, 0)
    goal = Vector2i(3, 3)
    blocked = {Vector2i(1, 2), Vector2i(3,2)}

    path = astar(start, goal, 10, 10, blocked)
    print("Path:", path)
