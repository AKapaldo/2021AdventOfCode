with open('D6.txt', "r") as f:
    input = f.read().split(',')
input = list(map(int, input))

def ocean(days):
    for _ in range(days):
        for f in range(len(input)):
            if input[f] > 0:
                input[f] -= 1
            elif input[f] < 1:
                input[f] = 6
                input.append(8)
    print(len(input))
            


ocean(256)
