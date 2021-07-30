def longestSubStrWithAtLeastKRepeatedChars(s, k):
    if k > len(s):
        return 0

    max_unique = len(set(s))
    result = 0

    for num_unique_expected in range(1, max_unique + 1):
        count_map = [0] * 26
        window_start, window_end, alphabet_index, num_curr_unique_in_window, numCharsInWindowWithAtLeastKRepeats = 0, 0, 0, 0, 0

        while window_end < len(s):
            if num_curr_unique_in_window <= num_unique_expected:   # if true, this flow expands the sliding window
                alphabet_index = ord(s[window_end]) - ord('a')     # provides the position (index) of where in the alphabet the current letter is
                char_count = count_map[alphabet_index]

                if char_count == 0:
                    num_curr_unique_in_window += 1

                new_char_count = char_count + 1                    
                count_map[alphabet_index] = new_char_count          # new char in window has been processed so update the count_map

                if new_char_count == k:
                    numCharsInWindowWithAtLeastKRepeats += 1

                window_end += 1
            else:                                                   # shrinks the sliding window
                alphabet_index = ord(s[window_start]) - ord('a')
                char_count = count_map[alphabet_index]

                if char_count == k:
                    numCharsInWindowWithAtLeastKRepeats -= 1

                new_char_count = char_count - 1
                count_map[alphabet_index] = new_char_count

                if new_char_count == 0:
                    num_curr_unique_in_window -= 1

                window_start += 1

            if num_curr_unique_in_window == num_unique_expected and num_curr_unique_in_window == numCharsInWindowWithAtLeastKRepeats:
                result = max(result, window_end - window_start)

    return result


def longestSubStrWithAtLeastKRepeatedCharsV2(s, k):
    if len(s) < k:
        return 0

    max_unique = len(set(s))
    result = 0

    for num_unique_expected in range(1, max_unique + 1):
        count_map = [0] * 26
        start, end, num_repeated_chars_in_window_at_least_k, num_unique_in_window = 0, 0, 0, 0

        while end < len(s):
            if num_unique_in_window <= num_unique_expected:
                alphabet_index = ord(s[end]) - ord('a')
                num_chars = count_map[alphabet_index]

                if num_chars == 0:
                    num_unique_in_window += 1

                num_chars += 1
                count_map[alphabet_index] = num_chars

                if num_chars == k:
                    num_repeated_chars_in_window_at_least_k += 1

                end += 1
            else:
                alphabet_index = ord(s[start]) - ord('a')
                num_chars = count_map[alphabet_index]

                if num_chars == k:
                    num_repeated_chars_in_window_at_least_k -= 1

                num_chars -= 1

                if num_chars == 0:
                    num_unique_in_window -= 1

                count_map[alphabet_index] = num_chars
                start += 1

            if num_unique_in_window == num_unique_expected and num_unique_in_window == num_repeated_chars_in_window_at_least_k:
                result = max(result, end - start)

    return result
