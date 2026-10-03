class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {

        // find the frequency of each element
        unordered_map<int, int> counts; // hashmap; frequency : num
        for (int num : nums) {
            counts[num]++;
        }

        vector<vector<int>> buckets(nums.size() + 1); 
        // a vector of vectors, outer index is the frequency
        // inner vectors are the elements of that frequency

        // starting from highest frequency, put elements into buckets
        for (const auto& [num, freq]: counts) {
            buckets[freq].push_back(num);
        }

        vector<int> result;
        // put into a result vector from the reverse order of bucket index, aka nums.size()
        for (int freq = nums.size(); freq >=0; freq--){

            for (int num: buckets[freq]) {
                result.push_back(num);
         
                if (result.size() == k) {
                    return result;
                }
            }
        }
        return result; 
        

        
        
    }
};
