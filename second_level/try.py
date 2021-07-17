# cook your dish here
for i in range(int(input())):
    no_of_games = int(input())
    for j in range(no_of_games):
        values = input().split(' ')
        head_count = 0
        tail_count = 0
        if not int(values[1]) % 2:
            head_count = int(values[1])//2
            tail_count = head_count
        else:
            if int(values[0]) == 1:
                head_count = int(values[1])//2
                tail_count = head_count + 1
            else:
                tail_count = int(values[1])//2
                head_count = tail_count + 1
        if int(values[2]) == 1:
            print(head_count)
        else:
            print(tail_count)