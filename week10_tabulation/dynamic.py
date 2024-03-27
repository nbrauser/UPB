rec_call_count = 0

 #  Recursive solution
def fib_num_rec(req_fib_num):
    global rec_call_count
    rec_call_count += 1
    if req_fib_num <= 1:
        return req_fib_num
    else:
        return fib_num_rec(req_fib_num - 2) + fib_num_rec(req_fib_num - 1)


# for num in [5, 10, 15, 20, 25]:
#    print(f"{num}th is {fib_num_rec(num)}")
#    print(f"total recursive calls: {rec_call_count:,}")
#    print('*'*500)


fib_val_memo = {}
memo_call_count = 0


 #  Memoization solution
def fib_num_memo(req_fib_num):
    global fib_val_memo
    global memo_call_count
    memo_call_count += 1

    if req_fib_num in fib_val_memo:
        return fib_val_memo[req_fib_num]
    elif req_fib_num <= 1:
        fib_val_memo[req_fib_num] = req_fib_num
        return req_fib_num
    else:
        fib_val_memo[req_fib_num] = fib_num_memo(req_fib_num - 2) + fib_num_memo(req_fib_num - 1)

        fib_val_memo = dict(list(fib_val_memo.items())[-2:])
    return fib_val_memo[req_fib_num]


for num in [5, 10, 15, 20, 25]:
    print(f"{num}th is {fib_num_rec(num)}")
    print(f"total recursive calls: {rec_call_count:,}")
    print('*'*500)
    print()

    memo_call_count = 0
    print(f"{num}th value is {fib_num_memo(num)}")
    print(f"total memo calls: {memo_call_count}")
    print(f"memo: {fib_val_memo}")
    print('*'*500)
    print()



