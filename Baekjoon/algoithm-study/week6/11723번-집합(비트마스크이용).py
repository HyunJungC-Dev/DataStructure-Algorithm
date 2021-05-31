import sys

m = int(sys.stdin.readline())
S = 0
for _ in range(m):
    cmd = sys.stdin.readline()  # op, *num = input().split() -> *붙이면 뒤에것을 배열로 받음 32이하

    if cmd == "all\n":
        S = (1 << 21)-1

    elif cmd == "empty\n":
        S = 0
    else:
        cmd, x = cmd.split(' ')
        x = int(x)
        if cmd == "add":
            S |= 1 << int(x)
        elif cmd == "check":
            if S & (1 << int(x)):
                print(1)
            else:
                print(0)
        elif cmd == "remove":
            S &= ~(1 << int(x))
        elif cmd == "toggle":
            S ^= (1 << int(x))
