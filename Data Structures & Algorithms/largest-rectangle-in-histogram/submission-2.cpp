#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = (int)heights.size();
        int ans = 0;

        stack<pair<int,int>> st;

        for (int i = 0; i < n; ++i) {
            int start = i;

            while (!st.empty() && st.top().second > heights[i]) {
                auto [j, h] = st.top();
                st.pop();
                ans = max(ans, h * (i - j));
                start = j;  
            }

            st.emplace(start, heights[i]);
        }

        while (!st.empty()) {
            auto [j, h] = st.top();
            st.pop();
            ans = max(ans, h * (n - j));
        }

        return ans;
    }
};
