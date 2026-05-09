func search(nums []int, target int) int {
    l, r := 0, len(nums)
    for l < r {
        m := l + (r - l ) / 2
        if nums[m] >= target{
            r = m
        } else{
            l = m + 1
        }
    }
    if l == len(nums) || nums[l] != target{
        return -1
    }
    return l
}
