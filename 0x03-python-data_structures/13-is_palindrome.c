#include "lists.h"

/**
* reverse_list - helper function to reverse a list
* @head: pointer to pointer to start on the list to reverse
*
* Return: pointer to listint_t
*/

listint_t *reverse_list(listint_t **head)
{
listint_t *prev = NULL;
listint_t *curr = *head;
listint_t *next;

while (curr != NULL)
{
	next = curr->next;
	curr->next = prev;
	prev = curr;
	curr = next;
}
*head = prev;
return (*head);
}

/**
* is_palindrome - Checking if linked list is palindrome
* @head: pointer to pointer to first node of linked list
*
* Return: integer
*/

int is_palindrome(listint_t **head)
{
listint_t *slow = *head;
listint_t *fast = *head;
listint_t *half;
listint_t *temp;

if (head == NULL || *head == NULL)
	return (1);

while (fast != NULL && fast->next != NULL)
{
	slow = slow->next;
	fast = fast->next->next;
}

if (fast != NULL)
	slow = slow->next;

half = reverse_list(&slow);
temp = half;

while (half != NULL)
{
	if (half->n != (*head)->n)
		return (0);
	half = half->next;
	*head = (*head)->next;
}

reverse_list(&temp);

return (1);
}
