// 83. Remove Duplicates from Sorted List

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* deleteDuplicates(struct ListNode* head){
    if(!head){
        return head;
    }
    struct ListNode* curr1 = head;
    struct ListNode* curr2 = head;
    while(curr1->next){
        curr1=curr1->next;
        if(curr2->val == curr1->val){
            while(curr2->val == curr1->val && curr1->next){
                curr1=curr1->next;
            }
            curr2->next = curr1; 
        }
        if(curr2->val == curr2->next->val){
            curr2->next = NULL;
        } else {
            curr2 = curr2->next;
        }
    }
    return head;
}