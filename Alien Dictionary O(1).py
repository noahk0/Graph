def foreignDictionary(self, words: List[str]) -> str:
    order, seen, graph = [''], {}, {letter: set() for word in words for letter in word}

    for i in range(1, len(words)):
        if len(words[i]) < len(words[i - 1]) and words[i][:len(words[i])] == words[i - 1][:len(words[i])]:
            return ''

        for j in range(min(len(words[i]), len(words[i - 1]))):
            if words[i][j] != words[i - 1][j]:
                graph[words[i][j]].add(words[i - 1][j])
                break

    def dfs(letter):
        if letter in seen:
            return seen[letter]

        seen[letter] = True

        for after in graph[letter]:
            if dfs(after):
                return True

        order[0] += letter
        seen[letter] = False

    for letter in graph:
        if dfs(letter):
            return ''

    return order[0]
