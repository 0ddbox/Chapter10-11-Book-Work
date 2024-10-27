def test_mutable_tuple():
    list0 = [1, 2, 3]
    list1 = [4, 5]
    t = (list0, list1)

    # Modify the second list in the tuple
    t[1].append(6)
    print(f"Modified tuple: {t}")

    try:

        d = {t: 'this tuple contains two lists'}
        print("Successfully created dictionary")
    except TypeError as e:
        print(f"TypeError occurred: {e}")


def shift_letter(letter, shift):

    if not letter.isalpha():
        return letter

    # Create letter to number mapping
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letter_map = dict(zip(letters, range(len(letters))))

    # Get the numeric position and shift it
    pos = letter_map[letter.lower()]
    new_pos = (pos + shift) % 26

    # Convert back to letter
    new_letter = letters[new_pos]

    # Preserve original capitalization
    return new_letter.upper() if letter.isupper() else new_letter


def shift_word(word, shift):
    shifted_letters = [shift_letter(letter, shift) for letter in word]
    return ''.join(shifted_letters)


def most_frequent_letters(text):
    # Count letter frequencies
    freq = {}
    for char in text.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1

    # Sort by frequency (descending) and then by letter (ascending)
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_freq


def find_anagrams(words):
    # Create dictionary mapping sorted letters to list of words
    anagram_map = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        anagram_map.setdefault(sorted_word, []).append(word)

    # Return only the groups that have at least two words
    return [word_list for word_list in anagram_map.values() if len(word_list) > 1]


def word_distance(word1, word2):
    if len(word1) != len(word2):
        raise ValueError("Words must have the same length")

    return sum(1 for c1, c2 in zip(word1, word2) if c1 != c2)


def find_metathesis_pairs(words):
    # First group words by their sorted letters (anagrams)
    anagram_map = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        anagram_map.setdefault(sorted_word, []).append(word)

    # Check each group of anagrams for metathesis pairs
    metathesis_pairs = []
    for word_list in anagram_map.values():
        if len(word_list) < 2:
            continue

        # Check each pair of words in the group
        for i, word1 in enumerate(word_list):
            for word2 in word_list[i + 1:]:
                if word_distance(word1, word2) == 2:
                    metathesis_pairs.append((word1, word2))

    return metathesis_pairs


def main():
    # Test mutable tuple
    print("Testing mutable tuple:")
    test_mutable_tuple()
    print()

    # Test Caesar cipher
    print("Testing Caesar cipher:")
    test_words = [
        ("cheer", 7),
        ("melon", 16),
    ]
    for word, shift in test_words:
        encrypted = shift_word(word, shift)
        print(f"'{word}' shifted by {shift} is '{encrypted}'")
    print()

    # Test letter frequency
    print("Testing letter frequency:")
    text = "The quick brown fox jumps over the lazy dog"
    frequencies = most_frequent_letters(text)
    print("Letter frequencies:")
    for letter, count in frequencies:
        print(f"'{letter}': {count}")
    print()

    # Test anagrams
    print("Testing anagrams:")
    test_words = [
        "deltas", "desalt", "lasted", "salted", "slated", "staled",
        "retainers", "ternaries", "generating", "greatening",
        "resmelts", "smelters", "termless"
    ]
    anagram_groups = find_anagrams(test_words)
    print("Anagram groups:")
    for group in anagram_groups:
        print(group)
    print()

    # Test word distance
    print("Testing word distance:")
    word_pairs = [
        ("hello", "hella"),
        ("python", "jython"),
    ]
    for word1, word2 in word_pairs:
        dist = word_distance(word1, word2)
        print(f"Distance between '{word1}' and '{word2}': {dist}")
    print()

    # Test metathesis pairs
    print("Testing metathesis pairs:")
    test_words = ["converse", "conserve", "python", "typhon"]
    pairs = find_metathesis_pairs(test_words)
    print("Metathesis pairs:")
    for pair in pairs:
        print(f"{pair[0]} <-> {pair[1]}")


if __name__ == '__main__':
    main()