#include<iostream>
#include<fstream>
using namespace std;

int main(){
string wordlist[46]={"a","i","at","an","see","saw","said","spoke","sense","mentioned","hello","hi","help","then","than","that","those","and","ate","eat","answer",
		"enter","entrance","open","because","however","the","be","to","of","in","it","for","not","on","with","as","this","by","from","they","we","say","or"
		"will","my","one"};
ofstream myfile("Dicts/myfile2.txt");
for (int i=0;i<46;i++){
myfile << wordlist[i];
myfile << '\n';
}
myfile.close();
return 0;
}
