from itertools import chain, combinations

def power_set(s):
    sorted_s = sorted(s)
    return list(chain.from_iterable(combinations(sorted_s, r) for r in range(len(sorted_s) + 1)))

def display_power_set(powerset):
    print("Power Set:")
    for subset in powerset:
        print(subset)

def main():
    user_input = input("Please enter the elements of a set, separated by spaces: ")
    user_set = set(user_input.split())
    powerset = power_set(user_set)
    display_power_set(powerset)

# Test cases
def run_tests():
    test_cases = [
        # Normal cases
        ({"a", "b"}, [(), ("a",), ("b",), ("a", "b")]),
        ({"1", "2", "3"}, [(), ("1",), ("2",), ("3",), ("1", "2"), ("1", "3"), ("2", "3"), ("1", "2", "3")]),
        ({"x", "y", "z"}, [(), ("x",), ("y",), ("z",), ("x", "y"), ("x", "z"), ("y", "z"), ("x", "y", "z")]),
        
        # Edge cases
        (set(), [()]),  # Empty set
        ({"a"}, [(), ("a",)]),  # Single element
        ({"1", "2"}, [(), ("1",), ("2",), ("1", "2")]),  # No duplicates
    ]

    for i, (input_set, expected_output) in enumerate(test_cases, 1):
        result = power_set(input_set)
        sorted_result = [tuple(sorted(subset)) for subset in result]
        sorted_expected = [tuple(sorted(subset)) for subset in expected_output]
        assert sorted(sorted_result) == sorted(sorted_expected), f"Test case {i} failed. Got {sorted_result}, expected {sorted_expected}."
        print(f"Test case {i} passed!")

if __name__ == "__main__":
    run_tests()
    main()




