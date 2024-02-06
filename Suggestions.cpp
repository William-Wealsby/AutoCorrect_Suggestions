#include<fstream>
#include<iostream>
#include<vector>
using namespace std;
extern "C"{
//function that provides a score to a word
int scoreword(string word, string testword){
int score = 0;

if(word.length()>testword.length()){
	score += 10*(word.length()-testword.length());
	for(int i=0; i<testword.length();i++){
		if(word[i]!=testword[i]){score+=10;}
	}}
if(testword.length()<=word.length()){
	score += 1*(testword.length()-word.length());
	for(int i=0; i<word.length();i++){
	if(word[i]!=testword[i]){score+=10;}}
}
return score;
}

//}
//extern "C"{

vector<string> suggest(string path,string word){

//reads file(at path) and enters all words into vector<string> dictionary for manipulation
string textline;
vector<string> dictionary;
ifstream myfile(path);
while(getline (myfile,textline)){
dictionary.push_back(textline);
}
myfile.close();


// to rank each word in the dictionary we implement a stack. 1 list contains the words added the the other their score
// words are only added if they have a better score that the last element of the list. Therefore the last element is the best 
// if the list is >3 words long then the last 3 elements are accepted. If it is 2 then 1 more stack is implemented and if 1 word comes up each time then 
// it makes another stack, if that also only results in 1 word than finally a third stack.
vector<string> temp;
vector<int> score;


vector<string> list;
list.push_back(dictionary[0]);
return list;


}}

int main(){
vector<string> words = suggest("Dicts/myfile.txt", "hi");
for (vector<string>::iterator itr=words.begin();itr<words.end();itr++){
cout << *itr <<'\n';
}

return 0;
}
