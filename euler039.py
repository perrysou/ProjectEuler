"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""

def integer_right_triangles(p):
    res = 0
    for a in range(3, p):
        for b in range(a, p - 2 * a):
            c = p - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print(a, b, c, p)
                res += 1
    return res

if __name__ == '__main__':
    inputs = raw_input().split("\n")
    number_test_cases = inputs[0]
    test_cases = inputs[1]
    print(test_cases)
    number_of_solutions = 0
    res = 0
    for t in test_cases:
        for i in range(t + 1):
            if integer_right_triangles(i) > number_of_solutions:
                number_of_solutions = integer_right_triangles(i)
                res = i
    print(res)
