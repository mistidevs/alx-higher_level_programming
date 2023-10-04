#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
* insert_node - insertng a node at a point while considering
* the numerical values of other nodes
* @head: pointer to pointer to the first node
* @number: number to add
*
* Return: pointer to created node
*/

listint_t *insert_node(listint_t **head, int number)
{
listint_t *curr, *temp;

if (*head == NULL)
{
	*head = malloc(sizeof(listint_t));
	if (*head == NULL)
		return (NULL);
	(*head)->n = number;
	(*head)->next = NULL;
	return (*head);
}

curr = *head;
while (curr != NULL)
{
	if (curr->next->n > number || curr->next == NULL)
	{
		temp = curr;
		curr = malloc(sizeof(listint_t));
		if (curr == NULL)
			return (NULL);
		curr->n = number;
		curr->next = temp;
		break;
	}
	curr = curr->next;
}

return (curr);
}
