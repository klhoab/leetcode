/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *p1, *p2, *root, *p;
        p1= l1; p2= l2;
        root = new ListNode(0);
        p = root;
        while (p1!= NULL || p2!= NULL){
            if (p->next== NULL) { 
                p->next = new ListNode(0);
            }
            p= p->next;
            if (p1) { p->val+= p1->val; p1= p1->next; }
            if (p2) { p->val+= p2->val; p2= p2->next; }
            if (p->val>=10) { p->next= new ListNode(1); p->val-=10; }
        }    
        return root->next;
    }
};
