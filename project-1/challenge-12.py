if __name__ == '__main__':
    n = int(input())
    lst = []
    for _ in range(n):
        command = input().split()
        cmd = command[0]
        args = list(map(int, command[1:]))

        if cmd == "insert":
            lst.insert(*args)
        elif cmd == "print":
            print(lst)
        elif cmd == "remove":
            lst.remove(*args)
        elif cmd == "append":
            lst.append(*args)
        elif cmd == "sort":
            lst.sort()
        elif cmd == "pop":
            lst.pop()
        elif cmd == "reverse":
            lst.reverse()
