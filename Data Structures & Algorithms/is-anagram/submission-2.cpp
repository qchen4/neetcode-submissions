class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int>  mps;
        unordered_map<char, int> mpt;

        for (char c: s){
            mps[c]++;
        }

        for (char c: t){
            mpt[c]++;
        }
        return mps == mpt;
    }
};
