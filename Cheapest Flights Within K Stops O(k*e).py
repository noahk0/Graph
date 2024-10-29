def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = defaultdict(dict)
        
    for flight in flights:
        graph[flight[0]][flight[1]] = flight[2]

    price = deepcopy(graph[src])
    new = set(price.keys())

    for _ in range(k):
        bfs, new, pre = new, set(), deepcopy(price)

        for source in bfs:
            for destination in graph[source]:
                new.add(destination)

                if destination not in price or pre[source] + graph[source][destination] < price[destination]:
                    price[destination] = pre[source] + graph[source][destination]

    return price[dst] if dst in price else -1
