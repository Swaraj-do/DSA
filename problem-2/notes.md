# 📝 Notes — Armstrong Number

🔗 **Problem Link:** [Armstrong Number — GeeksForGeeks](https://www.geeksforgeeks.org/problems/armstrong-number3918/1)

---

## 📌 What is an Armstrong Number?
- A 3-digit number where the **sum of cubes of its digits equals the number itself**
- Formula: if `n = abc` then `a³ + b³ + c³ == n`
- Example: 153 → 1³ + 5³ + 3³ = 1 + 125 + 27 = **153** ✅

---

## 📌 How to Extract Digits
Three ways to extract digits from a number:

**Using String conversion (easiest):**
```python
digits = [int(d) for d in str(n)]   # 153 → [1, 5, 3]
```

**Using Modulo & Division:**
```python
a = n % 10        # last digit
b = (n // 10) % 10  # middle digit
c = n // 100      # first digit
```

---

## 📌 Key Operators Used

| Operator | Meaning | Example |
|----------|---------|---------|
| `%` | Remainder | 153 % 10 = 3 |
| `//` | Floor division | 153 // 10 = 15 |
| `**` | Power | 3 ** 3 = 27 |

---

## 📌 Dry Run

### n = 153
```
digits = [1, 5, 3]
1³ + 5³ + 3³
= 1 + 125 + 27
= 153 == 153 ✅ → True
```

### n = 372
```
digits = [3, 7, 2]
3³ + 7³ + 2³
= 27 + 343 + 8
= 378 ≠ 372 ❌ → False
```

---

## 📌 List Comprehension (used in solution)
```python
[int(d) for d in str(n)]
```
- `str(n)` → converts number to string `"153"`
- `for d in str(n)` → loops over each character `"1"`, `"5"`, `"3"`
- `int(d)` → converts each character back to integer `1, 5, 3`

---

## 📌 sum() with Generator
```python
sum(d**3 for d in digits)
```
- Loops over each digit, cubes it, and sums all at once
- Cleaner than writing a separate loop

---

## 📌 Related Concepts to Explore
- [ ] Narcissistic Numbers (generalised Armstrong for n digits)
- [ ] Digit Extraction using Modulo
- [ ] List Comprehension
- [ ] String ↔ Integer Conversion
