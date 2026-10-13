def add(a: int, b: int) -> int:
    return a + b


def sub(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("MSIS DevOps demo project")
    print("add(5, 3) =", add(5, 3))
    print("sub(5, 3) =", sub(5, 3))
    print("multiply(5, 3) =", multiply(5, 3))
    print("divide(6, 3) =", divide(6, 3))


if __name__ == "__main__":
    main()
