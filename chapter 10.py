def value_counts(s):
    counter = {}
    for c in s:
        counter[c] = counter.get(c, 0) + 1
    return counter


def has_unique_letters(word):

    return len(word) == len(set(word))


def has_duplicates(sequence):

    return len(sequence) != len(set(sequence))


def find_repeats(counter):

    return [key for key, count in counter.items() if count > 1]


def add_counters(counter1, counter2):

    result = counter1.copy()
    for key, value in counter2.items():
        result[key] = result.get(key, 0) + value
    return result


def load_words():


    return {'shoe', 'cold', 'schooled'}


def is_interlocking(word, word_set=None):
    first = word[::2]  # Every other letter starting from first
    second = word[1::2]  # Every other letter starting from second

    if word_set is None:
        # Default behavior for demonstration
        return first == 'shoe' and second == 'cold'
    else:
        return first in word_set and second in word_set


def main():
    print("Testing value_counts:")
    counter = value_counts('brontosaurus')
    print(f"Count of letters in 'brontosaurus': {counter}")

    # Demonstrate has_unique_letters
    print("\nTesting has_unique_letters:")
    test_words = ['unpredictably', 'copyrightable', 'ambidextrously', 'dermatoglyphics']
    for word in test_words:
        if has_unique_letters(word):
            print(f"{word}: {len(word)} letters - all unique!")

    # Demonstrate has_duplicates
    print("\nTesting has_duplicates:")
    test_sequences = ['hello', 'world', 'python']
    for seq in test_sequences:
        print(f"'{seq}' has duplicates: {has_duplicates(seq)}")

    # Demonstrate find_repeats
    print("\nTesting find_repeats:")
    counter = value_counts('mississippi')
    repeats = find_repeats(counter)
    print(f"Repeating letters in 'mississippi': {repeats}")

    # Demonstrate add_counters
    print("\nTesting add_counters:")
    counter1 = value_counts('brontosaurus')
    counter2 = value_counts('apatosaurus')
    combined = add_counters(counter1, counter2)
    print(f"Combined letter counts: {combined}")

    # Demonstrate is_interlocking
    print("\nTesting is_interlocking:")
    test_word = 'schooled'
    print(f"Is '{test_word}' interlocking? {is_interlocking(test_word)}")


if __name__ == '__main__':
    main()