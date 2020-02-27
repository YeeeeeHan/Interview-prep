import random



def expected_matches(n):
    """ 
    :param n: number of persons
    :return: number of correct hat to correct person
    """
    matches = 0

    mylist1 = random.sample(range(1,n+1), n)    # array of unique persons
    mylist2 = random.sample(range(1,n+1), n)    # array of unique hats

    for i in range(0,n):
        if mylist1[i] == mylist2[i]:
            matches += 1

    return matches



if __name__ == '__main__':

    totalmatches = 0
    for _ in range (0,1000):
        totalmatches += expected_matches(20)

    print(f"Expected matches = {totalmatches/1000}")

