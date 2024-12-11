# recursion function
def rec_cnt(num):
    print(num)
    if num == 0:
        return 0
    rec_cnt(num - 1)


rec_cnt(5)
