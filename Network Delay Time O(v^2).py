def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    explored, graph = {k,}, defaultdict(dict)

    for time in times:
        graph[time[0]][time[1]] = time[2]

    candidate = graph[k]

    while candidate:
        new = min(candidate, key = candidate.get)
        explored.add(new)
        time = candidate.pop(new)

        for node in graph[new]:
            if node not in explored and (node not in candidate or time + graph[new][node] < candidate[node]):
                candidate[node] = time + graph[new][node]

    return time if n == len(explored) else -1
