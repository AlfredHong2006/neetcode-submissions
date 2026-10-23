#include <vector>
#include <string>
#include <unordered_map>
#include <stack>
using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack <int> st;
        for (int i =0; i < tokens.size(); i++){
            string t = tokens[i];
            if (t != "+" && t != "-" && t != "*" && t != "/"){
                st.push(stoi(t));

            }else{
                int a= int(st.top());
                st.pop();
                int b = int(st.top());
                st.pop();
                if (t == "+"){
                    st.push(a+b);
                }
                if (t == "-"){
                    st.push(b-a);
                }
                if (t == "/"){
                    st.push(int(b/a));
                }
                if (t == "*"){
                    st.push(a*b);
                }
            }
        }
        return int(st.top());
    }
};