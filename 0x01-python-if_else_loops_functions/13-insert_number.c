#include "lists.h"
#include <stdio.h>

/**
 * insert_node - insert a new node in a sort list
 * @head: head of linked list to insert
 * @number: number to insert
 * Return: the insert node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode;
	listint_t *actual;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	if (*head == NULL)
	{
		*head = newNode;
		newNode->next = NULL;
		return (newNode);
	}
	actual = *head;
	while (actual)
	{
		if (number <= actual->n)
		{
			newNode->next = actual;
			*head = newNode;
			return (newNode);
		}
		if ((number >= actual->n) && (actual->next == NULL))
		{
			newNode->next = NULL;
			actual->next = newNode;
			return (newNode);
		}
		if ((number >= actual->n) && (number <= actual->next->n))
		{
			newNode->next = actual->next;
			actual->next = newNode;
			return (newNode);
		}
		actual = actual->next;
	}
	return (NULL);
}