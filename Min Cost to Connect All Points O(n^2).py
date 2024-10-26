def minCostConnectPoints(self, points: List[List[int]]) -> int:
    cost, connected = 0, points.pop()

    for point in points:
        point.append(abs(connected[0] - point[0]) + abs(connected[1] - point[1]))

    while points:
        minimum = 0

        for i in range(1, len(points)):
            if points[i][2] < points[minimum][2]:
                minimum = i

        connected = points[minimum][:2]
        cost += points.pop(minimum)[2]
                
        for point in points:
            point[2] = min(point[2], abs(connected[0] - point[0]) + abs(connected[1] - point[1]))

    return cost
