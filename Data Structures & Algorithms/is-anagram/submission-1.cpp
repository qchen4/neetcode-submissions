class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int>  mps;
        unordered_map<char, int> mpt;

        for (char c : s) {
            if (mps.contains(c)) {
                mps.at(c) = mps.at(c) +1;
            } else {
                mps.insert({c, 1});
            }
        }

        for (char c : t) {
            if (mpt.contains(c)) {
                mpt.at(c) = mpt.at(c) +1;
            } else {
                mpt.insert({c, 1});
            }
        }

        return (mps == mpt);



        
        
    }
};
