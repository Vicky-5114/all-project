def hanoi(n, src, helper, target):
    if n == 1:
        print(f"Move Disk 1 from {src} to {target}")
        return 1
    x = hanoi(n - 1, src, target, helper)
    print(f"Move Disk {n} from {src} to {target}")
    y = hanoi(n - 1, helper, src, target)
    return x + y + 1


if __name__ == "__main__":
    # Loop from 1 to 4
    for i in range(1, 5):
        print(f"====== Total Steps: {hanoi(i, "stick-1", "stick-2", "stick-3")} ======")
