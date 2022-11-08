// 202. Happy Number

int isHappy(int n){
    int digit;
    int sum =0;
    while(1){
        while(n>0){
            digit = n % 10;
            sum += digit*digit;
            n = n / 10;
        }
        if(sum==1)
            return 1;
        // sad number will repeat 4, 16, 37, 58, 89, 145, 42, 20...
        else if (sum==4){
            return 0;
        }
        n = sum;
        sum=0;
    }
    return 0;
}