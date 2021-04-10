
def findMin(N, nums):
    if not nums:
        return
    minIdx = 0
    for j in range(1, N):
        if nums[j] < nums[minIdx]:
            minIdx = j
    return minIdx


def reverSort(elements, inputList):
    cost = 0
    for i in range(elements-1):
        j = findMin(elements-i, inputList[i:])
        j += i
        inputList[i:j+1] = inputList[i:j+1][::-1]
        cost += j-i+1
    return cost


tests = int(input())
for i in range(1, tests + 1):
    elements, inputList = int(input()), [int(s) for s in input().split(" ")]
    cost = reverSort(elements, inputList)
    print("Case #"+str(i)+":", cost)
