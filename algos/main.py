import math
from typing import List


def maxSubArray(nums):
    max_sum = None
    sum_table = set()

    if len(nums) == 1:
        return nums[0]

    for start in range(len(nums)):
        for i in range(len(nums) + 1):
            slice_arr = nums[start:i]

            if not slice_arr:
                continue

            curr_sum = sum(slice_arr)

            if curr_sum in sum_table:
                continue

            if max_sum is None:
                max_sum = curr_sum
            else:
                max_sum = max(curr_sum, max_sum)

            sum_table.add(curr_sum)

    return max_sum


def lengthOfLongestSubstring(s):
    window_start = 0
    max_length = 0
    char_index_map = {}

    for window_end in range(len(s)):
        curr_char = s[window_end]

        if curr_char in char_index_map:
            window_start = max(window_start, char_index_map[curr_char] + 1)

        char_index_map[curr_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


def minSubArrayLen(target, nums):
    start = 0
    min_len = math.inf
    curr_sum = 0

    for end, num in enumerate(nums):
        curr_sum += num

        while curr_sum >= target:
            min_len = min(min_len, end - start + 1)
            curr_sum = curr_sum - nums[start]
            start += 1

    if min_len != math.inf:
        return min_len

    return 0


def findMaxLenSubArray(nums1, nums2):
    max_len = 0
    len1 = len(nums1)
    len2 = len(nums2)

    for i in range(len1 + len2 - 1):
        start1 = max(0, len1 - i - 1)
        start2 = max(0, i - (len1 - 1))
        curr_cons = 0

        while start1 < len1 and start2 < len2:
            if nums1[start1] == nums2[start2]:
                curr_cons += 1
                max_len = max(max_len, curr_cons)
            else:
                curr_cons = 0

            start1 += 1
            start2 += 1

    return max_len


def getLenOfLongestSubstringWithRepeatedChars(str):
    if len(str) == 1:
        return 1

    max_sub_len = 1
    prev_char = str[0]
    cons_chars = 1

    for curr_char in str[1:]:
        if prev_char == curr_char:
            cons_chars += 1
        else:
            cons_chars = 1

        max_sub_len = max(max_sub_len, cons_chars)
        prev_char = curr_char

    return max_sub_len


def getLenOfLongestSubstringWithAtLeastKRepeatedChars(s, k):
    if k == 1:
        return len(s)
    elif len(s) == 1 and k > 1:
        return 0
    elif len(s) == 2 and 0 < k <= 2:
        return 2

    sub_map = set()
    max_sub_len = 0

    for start in range(len(s)):
        count_map = {k: 0 for k in 'abcdefghijklmnopqrstuvwxyz'}

        for end in range(start, len(s)):
            count_map[s[end]] = count_map[s[end]] + 1
            sub_str = s[start:end + 1]
            if sub_str not in sub_map:
                if doesSubStrMeetKCriteria(k, count_map):
                    max_sub_len = max(max_sub_len, len(sub_str))
                sub_map.add(sub_str)

    return max_sub_len


def doesSubStrMeetKCriteria(k, count_map):
    meets_k_count = 0
    letter_count = 0

    for freq in count_map.values():
        if freq > 0:
            letter_count += 1

        if freq >= k:
            meets_k_count += 1

        if meets_k_count != letter_count:
            return False

    return True


# input is a sorted array that removes duplicates in-place and returns new array length
def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return 1

    start_index = 0  # also acts as a unique found counter

    for i in range(1, len(nums)):
        if nums[start_index] != nums[i]:
            start_index += 1
            nums[start_index] = nums[i]

    return start_index + 1


# input is a sorted array that removes duplicates in-place that appeared more than two times and returns new array length
# [1,1,1,2,2,3]
def removeDuplicates2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return 1

    start_index = 0  # also acts as a unique found counter
    num_dups_found = 0
    i = 1

    for j in range(2, len(nums)):
        if nums[i - 1] != nums[j]:
            nums[i + 1] = nums[j]
            i += 1

    return i + 1


def mergeSortedArray(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m - 1] >= nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTwoSortedLinkedLists(l1, l2):
    newNodeStart = None
    newNodeCurr = None

    while l1 and l2:
        if l1.val <= l2.val:
            if newNodeStart is None:
                newNodeStart = ListNode(l1.val)
                newNodeCurr = newNodeStart
            else:
                newNodeCurr.next = ListNode(l1.val)
                newNodeCurr = newNodeCurr.next

            l1 = l1.next
        else:
            if newNodeStart is None:
                newNodeStart = ListNode(l2.val)
                newNodeCurr = newNodeStart
            else:
                newNodeCurr.next = ListNode(l2.val)
                newNodeCurr = newNodeCurr.next

            l2 = l2.next

    if newNodeStart:
        if l1 is None and l2:
            newNodeCurr.next = l2
        elif l1 and l2 is None:
            newNodeCurr.next = l1
    elif l1:
        newNodeStart = l1
    else:
        newNodeStart = l2

    return newNodeStart


def shiftingLetters(s: str, shifts: List[int]):
    char_arr = list(s)
    sum_shifts = 0

    for char_index in reversed(range(len(char_arr))):
        sum_shifts += shifts[char_index]
        char_pos_in_alphabet = ord(s[char_index]) - ord('a')
        num_shifts = sum_shifts % 26

        new_pos = char_pos_in_alphabet + num_shifts

        if new_pos > 25:
            new_pos = new_pos - 26

        new_char = chr(ord('a') + new_pos)
        char_arr[char_index] = new_char

    s = ''.join(char_arr)
    return s








# l1 = ListNode(1, ListNode(2, ListNode(4, None)))
# l2 = ListNode(1, ListNode(3, ListNode(4, None)))
# mergeTwoSortedLinkedLists(l1, l2)
