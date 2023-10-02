#include "lists.h"

/**
* check_cycle - checking if the cycle is present
* @list: pointer to struct of type listint_t
*
* Return: 1 if cycle is found and 0 if no cycle is found
*/

int check_cycle(listint_t *list)
{
listint_t *slow = list;
listint_t *fast = list;

while (slow && fast && fast->next)
{
	slow = slow->next;
	fast = fast->next->next;
	if (slow == fast)
		return (1);
}

return (0);
}
