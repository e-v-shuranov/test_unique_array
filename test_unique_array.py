

def find_next(nums , assumption):

    left =0
    if assumption > len(nums)-1:
        right = len(nums)-1
    else:
        right = assumption
    last_index = -1
    val = nums[0]

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == val:
            last_index = mid
            left = mid + 1
        else:
            right = mid - 1

    if last_index == len(nums) - 1:
        return -1
    else:
        return last_index + 1


nums = [0, 0, 0, 0, 0] #, 1, 1, 2, 3, 4]
print(find_next(nums, assumption = len(nums) - 1))

# assumption - is an avarage number of repetition in array
def count_unique(nums, assumption):
    if not nums:
        return 0

    n = len(nums)
    unique_count = 1
    current = nums[0]
    k = assumption

    i = 0
    qq = 0
    while i < n-1 and qq < 100:

        i = find_next(nums, assumption)
        nums = nums[i:]
        # print("i:",i, nums, unique_count)
        qq += 1
        if i == -1:
            return unique_count
        else:
            unique_count += 1
    return unique_count




nums = [1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 9, 9, 9]

print(count_unique(nums, 3))