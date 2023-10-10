#include "lists.h"

/**
* is_palindrome - Checking if linked list is palindrome
* @head: pointer to pointer to first node of linked list
*
* Return: integer
*/

int is_palindrome(listint_t **head)
{
listint_t *slow, *fast, *prev, *previous, *current, *next, *left, *right;

if (*head == NULL)
	return (1);

slow = fast = *head;
while (fast != NULL)
{
	prev = slow;
	fast = fast->next->next;
	slow = slow->next;
}
if (*head == slow)
	return (1);
prev->next = NULL;

previous = NULL;
current = slow;
while (current != NULL)
{
	next = current->next;
	current->next = previous;
	previous = current;
	current = next;
}

left = *head;
right = previous;
while (right != NULL || left != NULL)
{
	if (right->n != left->n)
		return (0);
	right = right->next;
	left = left->next;
}

return (1);
}
