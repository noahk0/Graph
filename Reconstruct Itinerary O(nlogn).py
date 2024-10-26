def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    itenerary, dfs, flight = [], ['JFK'], defaultdict(list)
        
    for ticket in sorted(tickets, reverse=True):
        flight[ticket[0]].append(ticket[1])

    while dfs:
        while flight[dfs[-1]]:
            dfs.append(flight[dfs[-1]].pop())

        itenerary.append(dfs.pop())

    return itenerary[::-1]
