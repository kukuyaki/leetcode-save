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
    bool hasCycle(ListNode *head) {
        ListNode *k=head;
        ListNode *w=head;
        while( k != nullptr && k->next != nullptr ){
            k=k->next->next;
            w=w->next;

            if(k==w){
                return true;
            }

        }
        return false;
    }
};
