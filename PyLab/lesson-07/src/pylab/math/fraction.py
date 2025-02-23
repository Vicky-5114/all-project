from __future__ import annotations
from typing import Callable, Union


class Fraction:
    """
    Fraction class.
    """

    def __init__(self, a: int, b: int, use_naive_gcd: bool = False):
        """
        Initialize a `Fraction` instance.

        Parameters
        ----------
        a : int
            The molecule.
        b : int
            The denominator.

        Raises
        ------
        TypeError
            `a` and `b` must be intergers.
        """
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("`a` and `b` must be integers.")
        self.a: int = a
        self.b: int = b
        self.gcd: Callable[[int, int], int] = (
            Fraction.gcd_naive if use_naive_gcd else Fraction.gcd_euclidean
        )

    def __str__(self) -> str:
        gcd: int = self.gcd(self.a, self.b)
        x, y = self.a // gcd, self.b // gcd
        return str(x) if y == 1 else f"{x} / {y}"

    def __add__(self, other: Union[Fraction, int, float]) -> Fraction:
        other = Fraction.other_to_frac(other)
        return Fraction(self.a * other.b + other.a * self.b, self.b * other.b)

    def __radd__(self, other: Union[Fraction, int, float]):
        return self + other

    def __sub__(self, other: Union[Fraction, int, float]):
        other = Fraction.other_to_frac(other)
        return Fraction(self.a * other.b - other.a * self.b, self.b * other.b)

    def __rsub__(self, other: Union[Fraction, int, float]):
        other = Fraction.other_to_frac(other)
        return other - self

    def __mul__(self, other: Union[Fraction, int, float]):
        other = Fraction.other_to_frac(other)
        return Fraction(self.a * other.a, self.b * other.b)

    def __rmul__(self, other: Union[Fraction, int, float]):
        return self * other

    def __truediv__(self, other: Union[Fraction, int, float]):
        other = Fraction.other_to_frac(other)
        return Fraction(self.a * other.b, self.b * other.a)

    def __rtruediv__(self, other: Union[Fraction, int, float]):
        other = Fraction.other_to_frac(other)
        return other / self

    @staticmethod
    def gcd_naive(a: int, b: int):
        """
        Calculate GCD using naive method.

        Parameters
        ----------
        a : int
            First number.
        b : int
            Second number.

        Returns
        -------
        int
            Greatest common divisor of a and b.
        """
        # Convert to absolute values since GCD is always positive
        a, b = abs(a), abs(b)

        # GCD can't be larger than the smaller number
        smaller = min(a, b)

        # Try each number from smaller number down to 1
        for i in range(smaller, 0, -1):
            # If i divides both a and b evenly, it's the GCD
            if a % i == 0 and b % i == 0:
                return i
        return 1

    @staticmethod
    def gcd_euclidean(a: int, b: int):
        """
        Calculate GCD using Euclidean algorithm.

        Parameters
        ----------
        a : int
            First number.
        b : int
            Second number.

        Returns
        -------
        int
            Greatest common divisor of a and b.
        """
        # Convert to absolute values
        a, b = abs(a), abs(b)

        # Euclidean algorithm states:
        # GCD(a,b) = GCD(b,r) where r is remainder of a/b
        while b:
            r = a % b
            a = b
            b = r
            # Python allows elegant swap and modulo in one line
            # This is equivalent to:
            # a, b = b, a % b

        return a

    @staticmethod
    def other_to_frac(obj: Union[Fraction, int, float]):
        """
        Convert other numerical types to Fraction.

        Parameters
        ----------
        obj : Union[Fraction, int, float]
            Number to convert to Fraction.

        Returns
        -------
        Fraction
            Converted fraction.

        Raises
        ------
        TypeError
            If obj is of unsupported type.
        """
        if type(obj) == Fraction:
            return obj
        if type(obj) == int:
            return Fraction(obj, 1)
        if type(obj) == float:
            p = 10 ** len(str(obj).split(".")[1])
            return Fraction(int(obj * p), p)
        raise TypeError(
            f"unsupported operand type(s): <class 'Fraction'> and {type(obj)}"
        )


if __name__ == "__main__":
    print("Testing Fraction module...")
    f1 = Fraction(1, 2)
    f2 = Fraction(6, 3)
    f3 = Fraction(1, -4)
    f4 = Fraction(-1, 4)
    print(f1 + f2)
    print(f1 - f2)
    print(f1 * f2)
    print(f1 / f2)
    print(f1 + 3)
    print(f1 - 3.2)
    print(f1 * False)
    print(f1 / True)
    print(3 + f1)
    print(3.2 - f1)
    print(True * f1)
    print(False / f1)
    print(0.5 + 1 / f2 * True - 4 * f3 + f4)
