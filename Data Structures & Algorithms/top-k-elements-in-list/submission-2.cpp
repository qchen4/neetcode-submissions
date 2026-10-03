class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        /* 1. Use a hashmap to count the occurance of each number. */
        unordered_map<int, int> counts; // freq : element
        for (int num: nums) {
            counts[num]++;
        }


        /* 2. for each of the frequencies create a bucket and put the elements into it.*/
        vector<vector<int>> buckets(nums.size() + 1); /* index is frequency, inner vector 
                                                        are the elements; add one 
                                                        because frequency indexed from 1 */
        for (const auto& [element, freq] : counts) {
            buckets[freq].push_back(element);
        } 

        /* 3. From high to low frequency, append the elements into the returning vector
        and stop at the k elements. */
        vector<int> result;

        for (int freq = buckets.size() - 1; freq >= 0; freq--) {
            for (int element : buckets[freq]) {
                result.push_back(element);
                if (result.size() == k) {
                    return result;
                }
            }
        }
        return result;
    }
};
