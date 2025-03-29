def next_greater_elements(nums):
    """Finds the next greater element for each number using a monotonic stack."""
    stack = []  # Stack to maintain the elements
    result = [-1] * len(nums)  # Initialize result with -1 (default value if no greater element)

    # Iterate through the list
    for i, num in enumerate(nums):
        # Pop elements from the stack that are smaller than the current number
        while stack and nums[stack[-1]] < num:
            index = stack.pop()
            result[index] = num  # Set the next greater element for that index

        # Push the index of the current number onto the stack
        stack.append(i)

    return result


# Example usage
nums = [4, 3, 2, 1, 5, 6]
print(next_greater_elements(nums))  # Output: [5, 5, 5, 5, 6, -1]
