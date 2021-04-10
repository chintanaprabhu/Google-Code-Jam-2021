
def calcPenalty(x, y, mural):
    penalty = 0
    if not mural:
        return 0
    prev = mural[0]
    for i in range(1, len(mural)):
        if mural[i] == '?':
            mural[i] = prev
        cr = prev+mural[i]
        if cr == "CJ":
            penalty += x
        if cr == "JC":
            penalty += y
        prev = mural[i]
    return penalty


tests = int(input())
for i in range(1, tests + 1):
    line = [s for s in input().split(" ")]
    penalty = calcPenalty(int(line[0]), int(line[1]), list(line[2]))
    print("Case #"+str(i)+":", penalty)
