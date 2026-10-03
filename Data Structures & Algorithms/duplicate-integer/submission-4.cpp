class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> hashset;

        for (int i = 0; i < nums.size(); i++) 
        {
            hashset.insert(nums[i]);
        }
        return hashset.size() != nums.size();

    }
};