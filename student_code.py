'''Representing graphs'''

node_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}

# Part 1: list of sets
def part_1_graph():
    graph = [
        {1, 4},     # a -> b, e
        {2},        # b -> c
        {1, 3, 4},  # c -> b, d, e
        set(),      # d
        set()       # e
    ]
    return graph


# Part 2: list of lists
def part_2_graph():
    graph = [
        [0, 1, 4],  # a -> a, b, e
        [2],        # b -> c
        [3, 4],     # c -> d, e
        [],         # d
        [0, 3]      # e -> a, d
    ]
    return graph


# Part 3: list of dicts (with edge weights)
def part_3_graph():
    graph = [
        {1: 1, 2: 2, 4: 4, 0: 8},  # a -> b(1), c(2), e(4), a(8)
        {2: 3},                    # b -> c(3)
        {4: 4},                    # c -> e(4)
        {},                        # d
        {0: 1}                     # e -> a(1)
    ]
    return graph


# Part 4: dict of sets
def part_4_graph():
    graph = {
        'a': {'b', 'c', 'e'},
        'b': {'c'},
        'c': {'a'},
        'd': set(),
        'e': {'c'}
    }
    return graph


# Part 5: dict of dicts (with edge weights)
def part_5_graph():
    graph = {
        'a': {'b': 5, 'e': 6},
        'b': {'e': 2},
        'c': {},
        'd': {},
        'e': {'b': 3}
    }
    return graph

