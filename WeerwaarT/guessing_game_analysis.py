import random
import collections

# Constants for game runs and guessing boundaries
RUNS = 1_000_000
LOWER_BOUND = 1
UPPER_BOUND = 100

def binary_search_game(run: int, use_random_offset: bool = False) -> float:
    """Simulate the guessing game using binary search."""
    total_gain = 0

    for _ in range(run):
        num = random.randint(LOWER_BOUND, UPPER_BOUND)
        left, right = LOWER_BOUND, UPPER_BOUND
        guess_count = 0

        while left <= right:
            offset = right - left
            if use_random_offset and offset % 2 == 1:
                offset += 1 if random.random() >= 0.5 else -1

            mid = left + offset // 2

            guess_count += 1

            if mid == num:
                total_gain += 6 - guess_count
                break
            elif num < mid:
                right = mid - 1
            else:
                left = mid + 1

    return total_gain / run

def count_guesses() -> collections.Counter:
    """Count guesses required and calculate the expected gain."""
    guesses = []

    for i in range(LOWER_BOUND, UPPER_BOUND + 1):
        left, right = LOWER_BOUND, UPPER_BOUND
        guess_count = 0

        while left <= right:
            mid = left + (right - left) // 2
            guess_count += 1

            if mid == i:
                guesses.append(6 - guess_count)
                break
            elif i < mid:
                right = mid - 1
            else:
                left = mid + 1

    guess_counter = collections.Counter(guesses)
    total_gain = sum(award * count for award, count in guess_counter.items())
    expected_gain = total_gain / (UPPER_BOUND - LOWER_BOUND + 1)
    print(f"Expected gain after evaluating all numbers: {expected_gain:.6f}")

    return guess_counter

if __name__ == '__main__':
    # Run game 1 (standard binary search)
    result_game_1 = binary_search_game(RUNS)
    print(f"Game 1 - Approximated expectation after {RUNS} runs: {result_game_1:.6f}")

    # Run game 2 (random offset search)
    result_game_2 = binary_search_game(RUNS, use_random_offset=True)
    print(f"Game 2 - Approximated expectation after {RUNS} runs: {result_game_2:.6f}")

    # Count guesses and calculate expected gain
    guess_distribution = count_guesses()
    print(guess_distribution)
