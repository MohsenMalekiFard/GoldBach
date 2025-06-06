def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def goldbach_pair_exists(even_num):
    for p in range(2, even_num // 2 + 1):
        q = even_num - p
        if is_prime(p) and is_prime(q):
            return (p, q)
    return None

def test_goldbach(limit):
    for even in range(4, limit + 1, 2):
        pair = goldbach_pair_exists(even)
        if pair:
            print(f"{even} = {pair[0]} + {pair[1]}  → True")
        else:
            print(f"❌ {even} has no valid prime pair! (Potential counterexample)")

# ============================
# 👇 اجرای برنامه
n = int(input("یک عدد زوج بالا وارد کن (مثلاً 1000): "))
test_goldbach(n)
