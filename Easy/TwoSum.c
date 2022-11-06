// 1. Two Sum

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>

void merge(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
 
    int L[n1], R[n2];
 
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    i = 0;
    j = 0; 
    k = l; 
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
 

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
 

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}
 

void mergeSort(int arr[], int l, int r)
{
    if (l < r) {

        int m = l + (r - l) / 2;

        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
 
        merge(arr, l, m, r);
    }
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    *returnSize=2;
    int* output = (int*) malloc((*returnSize) * sizeof(int));
    output[0] = -1;
    output[1] = -1;
    int* orgArr = (int*) malloc(numsSize * sizeof(int));
    for(int i=0;i<numsSize;i++){
        orgArr[i] = nums[i];
    }
    mergeSort(nums,0,numsSize-1);
    int i=0; 
    int j=numsSize-1;
    while (i<numsSize && j>=0){
        if(nums[i]+nums[j]<target){
            i++;
        } else if (nums[i]+nums[j]>target){
            j--;
        } else {
            break;
        }
    }
    int first = nums[i];
    int second = nums[j];
    for(int i=0;i<numsSize;i++){
        if(output[0] != -1 && output[1] != -1){
            break;
        }
        if(output[0]==-1 && orgArr[i]==first){
            output[0] = i;
        } else if (output[1]==-1 && orgArr[i]==second){
            output[1] = i;
        }
    }

    return output;
}


/*
Brute force
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    *returnSize=2;
    int* output = (int*) malloc((*returnSize) * sizeof(int));
    for(int i=0; i<numsSize; i++){
        for(int j=i+1; j<numsSize; j++){
            if(nums[i] + nums[j] == target){
                output[0] = i;
                output[1] = j;
                break;
            }
        }
    }
    return output;
}
*/