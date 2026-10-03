class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int duplicate = -1;
        int missing = -1;

        unordered_map<int, int> mp;
        for (int i = 0; i < nums.size(); i++) {
            int current = nums[i];
            if (mp.contains(current))
            {
                duplicate = nums[i];
                mp.at(current) = mp.at(current) +1;
            } else {
                mp.insert({current, 1});
            }
    
        }
        return (duplicate != -1);



        
    }
};