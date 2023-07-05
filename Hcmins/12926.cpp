#include <string>
#include <vector>

using namespace std;

string solution(string s, int n) {
    char c;
    vector<char> v(s.begin(),s.end());
    for (char &c: v) {
        if('a'<=c && c<='z'){
            c=(c-'a'+n)%26+'a';
        }
        else if('A'<=c && c<='Z'){
            c=(c-'A'+n)%26+'A';
        }
        else{
            continue;
        }
        
    }
    
    string answer(v.begin(),v.end());
    return answer;
}

//https://school.programmers.co.kr/learn/courses/30/lessons/12926