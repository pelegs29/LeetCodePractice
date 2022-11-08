// 203. Remove Linked List Elements

/**
* Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* removeElements(struct ListNode* head, int val) 
{
    struct ListNode **curr = &head;
    while(*curr){
        struct ListNode *subCurr = *curr;
        if(subCurr->val == val){
            *curr=subCurr->next;
        } else {
            curr = &subCurr->next;
        }
    }
    return head;
}
