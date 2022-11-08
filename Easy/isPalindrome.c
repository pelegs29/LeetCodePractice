// 125. Valid Palindrome

#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>


bool isPalindrome(char * s){
    int len = strlen(s);
    if(!len || len ==1)
        return true;
    char* t = s + (len-1);
    while(s<t){
        if(!isalnum(*s)){s++;continue;}
        if(!isalnum(*t)){t--;continue;}
        if(tolower(*s++) != tolower(*t--)) return false;
    }
    return true;
}