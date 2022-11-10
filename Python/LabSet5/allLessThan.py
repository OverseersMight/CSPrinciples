
def all_less_than(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return False
    return True
def tester():
    listA = [45, 20, 300]
    listB = [50, 41, 600]
    print(all_less_than(listA, listB))

    listA2 = [32131, 312321, 321321]
    listB2 = [44554, 65, 412]
    print(all_less_than(listA2, listB2))

tester()