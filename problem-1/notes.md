# 📝 Notes — Prime Number

🔗 **Problem Link:** [Prime Number — GeeksForGeeks](https://www.geeksforgeeks.org/problems/prime-number2314/1)

---

## 📌 What is a Prime Number?
- A number **greater than 1** that has **no divisors other than 1 and itself**
- 2 is the **only even prime number**
- 1 is **not prime** (only one divisor)
- 0 and negatives are **not prime**

---

## 📌 What is a Composite Number?
- A number **greater than 1** that has **more than two divisors**
- Example: 4 → divisors are 1, 2, 4

---

## 📌 Divisibility Rule
- If `n % i == 0` for any `i` between 2 and n-1, then `n` is **not prime**
- `%` is the modulo operator — gives the **remainder** of division

---

## 📌 Why Check Only up to √n?
- If `n = a × b`, one of them must be ≤ √n
- So if no divisor is found up to √n, none will be found beyond it
- Example: n = 36 → √36 = 6 → divisors (2,18), (3,12), (4,9), (6,6) — one always ≤ 6

---

## 📌 6k ± 1 Rule
All integers can be written as one of:
```
6k, 6k+1, 6k+2, 6k+3, 6k+4, 6k+5
```
- `6k`   → divisible by 6 ❌
- `6k+2` → divisible by 2 ❌
- `6k+3` → divisible by 3 ❌
- `6k+4` → divisible by 2 ❌
- `6k+1` and `6k+5 (= 6k-1)` → only candidates ✅

So we only need to check `i` and `i+2` per loop, jumping by 6.

---

## 📌 Modulo Operator ( % )
| Expression | Result | Meaning |
|-----------|--------|---------|
| 10 % 2 | 0 | 10 is divisible by 2 |
| 10 % 3 | 1 | 10 is not divisible by 3 |
| 7 % 7 | 0 | 7 is divisible by itself |

---

## 📌 Key Number Theory Facts
- Every number > 1 is either prime or can be expressed as a product of primes
- There are infinitely many prime numbers
- The only even prime is **2**
- Twin primes — primes that differ by 2 (e.g. 11 & 13, 17 & 19)

---

## 📌 Complexity Comparison

| Approach | Time | Good For |
|----------|------|----------|
| Brute Force | O(n) | n < 1,000 |
| Square Root | O(√n) | n < 10⁶ |
| 6k ± 1 | O(√n) | n up to 10⁹ ✅ |
| Sieve | O(n log log n) | finding all primes in range |

---

## 📌 Related Concepts to Explore
- [ ] Sieve of Eratosthenes
- [ ] GCD & LCM
- [ ] Prime Factorisation
- [ ] Euler's Totient Function
- [ ] Modular Arithmetic
