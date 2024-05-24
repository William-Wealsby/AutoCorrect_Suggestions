#include<stdio.h>

int length(char* word){
    int length = 0;
    while(word[length]!='\n'){
        length++;
    }
    return length;
}

float evaluate(char* word,char* test){
    int len_word;
    int len_test;
    len_word = length(word);
    len_test = length(test);
    float eval  = 0;
    int chars = 0;
    if (len_test == len_word){chars = len_word;}
    if (len_test < len_word){// when len_test is less that len_word, reduce eval by the difference
        chars = len_test;
        eval -= len_word-len_test;
    }
    if (len_test > len_word){// when test length greater reduce value by a tenth of difference
        chars = len_word;
        eval -= (len_test-len_word)/(double)10;
    }
    for (int i=0;i<chars;i++){
        if (word[i]==test[i]){eval++;}
    }
    return eval;
}

void search(char* word, char* dict, char* return_string){
    FILE *fptr;
    char temp[20];
    fptr = fopen(dict, "r");
    if (fptr != NULL){
        while(fgets(temp, 20, fptr)) {
            printf("%s", temp);
        }
    }
    else {
        printf("Unable to open file\n");
        }
    fclose(fptr);
}



