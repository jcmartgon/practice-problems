# Jesus Carlos Martinez Gonzalez
# 18/06/2023
# Set Mutations ()

if __name__ == "__main__":
    n = int(input())
    a = set(input().split())
    m = int(input())

    for _ in range(m):
        cmd = input().split()
        b = set(input().split())
        match cmd[0]:
            case "update":
                a.update(b)
            case "intersection_update":
                a.intersection_update(b)
            case "symmetric_difference_update":
                a.symmetric_difference_update(b)
            case "difference_update":
                a.difference_update(b)

    print(sum(list(map(int, a))))
