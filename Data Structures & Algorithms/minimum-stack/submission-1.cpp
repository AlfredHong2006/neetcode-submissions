class MinStack {
private:
    stack<int> st;
    vector<int> minimum;

public:
    MinStack() {

    }
    
    void push(int value) {
        st.push(value);
        if (minimum.size() !=0){
            minimum.push_back(min(value, minimum.back()));
        }else{
            minimum.push_back(value);
        }
    }
    
    void pop() {
        minimum.pop_back();
        st.pop();
    }
    
    int top() {
        return st.top();
    }
    
    int getMin() {
        return minimum.back();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(value);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */