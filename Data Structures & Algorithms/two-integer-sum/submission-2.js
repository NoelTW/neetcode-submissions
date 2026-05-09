class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = {}
        for (const [index, ele] of nums.entries()){
            let diff = target - ele
            if (diff in map) {
                return [map[diff], index]
            }
            map[ele] = index
        } 
    }
    // O(n) O(n)
}

