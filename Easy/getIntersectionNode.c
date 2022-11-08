// 160. Intersection of Two Linked Lists

/**
* Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

int getListSize(struct ListNode *head){
    int size=0;
    while(head->next){
        size++;
        head=head->next;
    }
    return size+1;
}


struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    int sizeA = getListSize(headA);
    int sizeB = getListSize(headB);
    int diff;
    if(sizeA > sizeB){
        diff = sizeA-sizeB;
        for(int i=0;i<diff;i++){
            headA=headA->next;
        }
    } else if (sizeA < sizeB){
        diff = sizeB-sizeA;
        for(int i=0;i<diff;i++){
            headB=headB->next;
        }
    }
    while(headA && headB){
        if(headA==headB){
            return headA;
        }
        headA=headA->next;
        headB=headB->next;
    }
    return NULL;
    
}