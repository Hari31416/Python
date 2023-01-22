from prime import is_prime

colors = {
    "pass": "\033[92m",
    "fail": "\033[91m",
    "warning": "\033[93m",
    "end": "\033[0m",
    "bold": "\033[1m",
    "underline": "\033[4m",
}


def tests():
    try:
        assert is_prime(0) == False, "0 is not prime"
        assert is_prime(1) == False, "1 is not prime"
        assert is_prime(2) == True, "2 is prime"
        assert is_prime(3) == True, "3 is prime"
        assert is_prime(4) == False, "4 is not prime"
        assert is_prime(99990001) == True, "99990001 is prime"
        assert is_prime(99990002) == False, "99990002 is not prime"
        print(colors["pass"] + "All tests passed!" + colors["end"])
    except AssertionError as e:
        print(colors["fail"] + "Tests failed:" + colors["end"])
        print(e)


if __name__ == "__main__":
    tests()
