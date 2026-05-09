class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) {
            return false;
        }
        const left = {};
        const right = {};
        for (let s_item of s) {
            if (s_item in left) {
                left[s_item] += 1;
            } else {
                left[s_item] = 0;
            }
        }
        
        for (let t_item of t) {
            if (t_item in right) {
                right[t_item] += 1;
            } else {
                right[t_item] = 0;
            }
        }

        for (const key in right) {
            if (left[key] !== right[key]) {
                return false;
            }
        }
        return true;
    }
}
