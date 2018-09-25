# -*- coding: utf-8 -*-
"""Project Euler: Problem 94

Find the sum of the perimeters of all almost equilateral triangles
(with two sides equal and the third differing by no more than one unit)
with integral side lengths and area and whose perimeters do not exceed
one billion (1,000,000,000).

https://projecteuler.net/problem=94
"""


def main():
    """
    INITIAL ANALYSIS:
        For the triangle to be almost-equilateral, the three edges must
        have length (a, a, a + 1) or (a, a, a - 1).

        First looking at the case with (a, a, a + 1); from the Pythagorean
        theorem, we can write the following relation between a and triangle
        height h:
            h² + [(a + 1)/2]² = a²
            h² + (a + 1)²/4 = a²
            h² + a²/4 + a/2 + 1/4 = a²
            1 = 4a² - a² - 2a - 4h²
            3a² - 2a - 4h² = 1              | ×3
            9a² - 6a - 12h² = 3             | +1
            9a² - 6a + 1 - 12h² = 4         | /4
            [(3a - 1)/2]² - 3h² = 1
        Let x = (3a - 1)/2:
            x² - 3h² = 1
        A similar process can be done for (a, a, a - 1), and the result is
        the same, but x = (3a + 1)/2

    SOLVING DIOPHANTINE EQUATION:
        This equation can be solved iteratively, where in our case k=3:
            xₙ₊₁ = x₁xₙ + kh₁hₙ
            hₙ₊₁ = x₁hₙ + h₁xₙ
        Once the candidates are found, it is easy to revert back to
        length of edge. From the On-line Encyclopedia of Integer
        Sequences, we can find that the initial values are (2, 1).

    FINDING CANDIDATES:
        Once we have found possible x values, we can revert back to
        edge length and therefore, area:
            (a, a, a + 1)           or      (a, a, a - 1)
            a = (2x + 1)/3          or      a = (2x - 1)/3
            A = 0.5h(a + 1)         or      A = 0.5h(a - 1)
            A = h(x + 2)/3          or      A = h(x - 2)/3
        Which has to be integral. Additionally, a has to be integral.
        Finally, the perimeter of the triangle can't exceed 1 billion:
            s = a + a + (a ± 1) < 1,000,000,000
            3a ± 1 < 10⁹
            (3a ± 1)/2 < 5×10⁸
            x < 5×10⁸

    SOURCES:
        https://en.wikipedia.org/wiki/Pell's_equation#Additional_solutions_from_the_fundamental_solution]
        https://oeis.org/A002350
        https://oeis.org/A002349
    """
    perimeters = 0
    x1, h1 = 2, 1
    x, h = x1, h1
    while x < 500_000_000:
        # Case 1: (a, a, a + 1)
        a = (2 * x + 1) / 3
        A = h * (x + 2) / 3
        # Exclude (1, 1, 2)
        if A == int(A) and a == int(a) and a > 1:
            perimeters += 3 * a + 1

        # Case 2: (a, a, a - 1)
        a = (2 * x - 1) / 3
        A = h * (x - 2) / 3
        # Exclude (1, 1, 0)
        if A == int(A) and a == int(a) and a > 1:
            perimeters += 3 * a - 1

        # Calculate next solution to Diophantine equation
        x, h = x1 * x + 3 * h1 * h, x1 * h + h1 * x

    print(int(perimeters))


if __name__ == "__main__":
    main()
