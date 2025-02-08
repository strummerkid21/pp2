def solve(numheads, numlegs):
    y = (numlegs - 2 * numheads) // 2
    x = numheads - y
    return x, y
chickens, rabbits = solve(35, 94)
print(f"Chickens: {chickens}, Rabbits: {rabbits}")