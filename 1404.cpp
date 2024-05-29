#include <iostream>
#include <math.h>
#include <string>
using namespace std;
class Solution {
public:
    int numSteps(string s) {
        int count=0;
        int carry=0;
        int l=size(s)-1;
        while(l>0){
            if(s[l]-'0' + carry == 0){
                count++;
                carry=0;
            }
            else if(s[l]-'0' + carry == 2){
                count++;
                carry=1;
            }
            else{
                count+=2;
                carry=1;
            }
            l--;
        }
        if(carry==1){
            count++;
        }
    return count;
    }
};
