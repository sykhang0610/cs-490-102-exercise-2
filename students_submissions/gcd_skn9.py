def gcd(a: int, b: int) -> int:
   
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: inputs must be integers")
        return None

    if a == 0 and b == 0:
        return None

    # Make gcd non-negative
    a, b = abs(a), abs(b)

    if b == 0:
        return a

    # Recursive step
    return gcd(b, a % b)

if __name__ == "__main__":
    print(gcd(0, 0))        # None
    print(gcd(-54, 24))     # 6
    print(gcd(54, -24))     # 6
    print(gcd(-54, -24))    # 6
