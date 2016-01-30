#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <stack>
#include <string>
using namespace std;

class Palindrome {
    //Write your code here
public:
	//Pushes a character onto a stack
	void pushCharacter(char ch)
	{
		s.push(ch);
	}
	//Enqueues a character in a queue
	void enqueueCharacter(char ch)
	{
		q.push(ch);
	}
	//Pops and returns the top characte
	char popCharacter()
	{
		char c = s.top();
		s.pop();
		return c;
	}
	//Dequeues and returns the first character
	char dequeueCharacter()
	{
		char c = q.front();
		q.pop();
		return c;
	}
private:
	stack<char> s;
	queue<char> q;
};

int main() {
    // read the string s.
    string s;
    getline(cin, s);
    
  	// create the Palindrome class object p.
    Palindrome p;
    
    // push all the characters of string s to stack.
    for (int i = 0; i < s.length(); i++) {
        p.pushCharacter(s[i]);
    }
    
    // enqueue all the characters of string s to queue.
    for (int i = 0; i < s.length(); i++) {
        p.enqueueCharacter(s[i]);
    }
    
    bool f = true;
    
    // pop the top character from stack.
    // dequeue the first character from queue.
    // compare both the characters.
    for (int i = 0; i < s.length(); i++) {
        if (p.popCharacter() != p.dequeueCharacter()) {
            f = false;
            
            break;
        }
    }
    
    // finally print whether string s is palindrome or not.
    if (f) {
        cout << "The word, " << s << ", is a palindrome.";
    } else {
        cout << "The word, " << s << ", is not a palindrome.";
    }
    
    return 0;
}