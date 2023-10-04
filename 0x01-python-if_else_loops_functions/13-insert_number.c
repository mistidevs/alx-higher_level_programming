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
listint_t *new_node;
listint_t *current;
listint_t *previous;

new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
	return (NULL);

new_node->n = number;
new_node->next = NULL;

if (*head == NULL)
{
	*head = new_node;
	return (new_node);
}

current = *head;
previous = NULL;

while (current != NULL && current->n < number)
{
	previous = current;
	current = current->next;
}

if (previous == NULL)
{
	new_node->next = *head;
	*head = new_node;
}
else
{
	new_node->next = current;
	previous->next = new_node;
}

return (new_node);
}
