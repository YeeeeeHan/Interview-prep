# Complete the whatFlavors function below.
def whatFlavors(cost, money, dict):
    for i in range(1, n):
        value_to_search = money - cost[i]
        if cost_dict.get(value_to_search, None) is not None:
            if (cost_dict.get(value_to_search) > i):      # ensure value_to_search is not cost[i]
                print(i, dict[value_to_search])
                break




if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))
        cost.insert(0, None)

        cost_dict = {element: index for index, element in enumerate(cost) }

        whatFlavors(cost, money, cost_dict)

