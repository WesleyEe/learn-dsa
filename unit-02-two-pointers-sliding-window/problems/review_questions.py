# Given an array of integers nums and an integer k
# find the number of contiguous subarrays whose sum equals exactly k.


def review_qn_one(input_arr, target):
    # The idea here
    # Scan input arr from left to right, and build up a dict with the running total as the key and the number of times as total as the value
    # For each value in the input arr, find out if the running total minus the target is equal to a key that is in the dict
    # If it is, add that key's value onto the num_subarr
    # Return num_subarr

    num_subarr = 0
    dict_running_totals = {0: 1}
    running_total = 0

    for num in input_arr:
        running_total += num
        possible_running_total = running_total - target

        if possible_running_total in dict_running_totals:
            num_subarr += dict_running_totals[possible_running_total]

        if running_total not in dict_running_totals:
            dict_running_totals[running_total] = 1
        else:
            dict_running_totals[running_total] += 1

    return num_subarr


# Given a sorted array of integers nums, find if there exists a pair of
# indices i != j such that nums[i] + nums[j] equals a given target, returning True/False.


def review_qn_two(input_arr, target):

    left_ptr_idx = 0
    right_ptr_idx = len(input_arr) - 1

    while left_ptr_idx < right_ptr_idx:
        sum_of_ptr = input_arr[left_ptr_idx] + input_arr[right_ptr_idx]
        if sum_of_ptr == target:
            return True
        elif sum_of_ptr < target:
            left_ptr_idx += 1
        else:
            right_ptr_idx -= 1

    return False
