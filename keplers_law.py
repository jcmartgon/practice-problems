# Jesus Carlos Martinez Gonzalez
# 18/03/2024
# Kepler's Law (https://www.codechef.com/problems/KEPLERSLAW)

"""
Keplers Law states that the planets move around the sun in elliptical orbits with the sun at one focus.
Kepler's 3rd law is The Law of Periods, according to which:
• The square of the time period of the planet is directly proportional to the cube of the semimajor
axis of its orbit.
You are given the Time periods (Tl, T2) and Semimajor Axes (RI, R2) of two planets orbiting the same
star.
Please determine if the Law of Periods is satisfied or not, i.e. if the constant of poportionality of both
planets is the same.
Print "Yes" (without quotes) if the law is satisfied, else print "No".
"""

for _ in range(int(input())):
    t1, t2, r1, r2 = map(int, input().split())

    cp1 = pow(t1, 2) / pow(r1, 3)
    cp2 = pow(t2, 2) / pow(r2, 3)

    print("Yes" if cp1 == cp2 else "No")
