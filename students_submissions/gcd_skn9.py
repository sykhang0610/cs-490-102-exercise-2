def gcd(a: int, b: int) -> int:
    if b==0:
        return a
    return gcd(b,a%b)

print (gcd(12,16)) # Should be 4
print (gcd(123216,2352)) # Should be 48
print (gcd(1230,230)) # Should be 10
