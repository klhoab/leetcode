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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *head = new ListNode();
        ListNode *curr = head;
        
        while (l1 && l2){
            if (l2->val > l1->val){
                curr->next = l1;
                l1 = l1->next;
            }
            else {
                curr->next = l2;
                l2 = l2->next;
            }
            curr= curr->next;
                
        }
        
        curr->next = (l1 ? l1 : l2);
        curr = head->next;
        delete head;
        
        return curr;
    }
};
