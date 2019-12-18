#include "lists.h"
/**
 * is_palindrome - check if a list is a palindrome
 * @head: double pointer to head of list
 * Return: 1 or 0 depends on the case
 */
int is_palindrome(listint_t **head)
{
	listint_t *tortoise = *head, *hare = *head, *prev = *head, *tmp1;
	listint_t *list_2 = NULL, *mid_list = NULL, *actual, *tmp, *tmp2;
	int ret = 0;

	if (hare == NULL || hare->next == NULL)
		return (1);
	while (hare != NULL && hare->next != NULL)
		hare = hare->next->next, prev = tortoise, tortoise = tortoise->next;
	if (hare != NULL)
		mid_list = tortoise, tortoise = tortoise->next;
	list_2 = tortoise, prev->next = NULL;
    prev = NULL; actual = list_2;
    while (actual)
	    tmp = actual->next, actual->next = prev, prev = actual, actual = tmp;
	list_2 = prev;
    tmp1 = *head, tmp2 = list_2; 
    while (tmp1 != NULL && tmp2 != NULL)
	{
		if (tmp1->n == tmp2->n)
			tmp1 = tmp1->next, tmp2 = tmp2->next;
		else
			ret = 0;
	}
	if (tmp1 == NULL && tmp2 == NULL)
		ret = 1;
	else 
        ret = 0;
	prev = NULL; actual = list_2;
    while (actual)
	    tmp = actual->next, actual->next = prev, prev = actual, actual = tmp;
	list_2 = prev;
	if (mid_list)
		prev->next = mid_list, mid_list->next = list_2;
	else
		prev->next = list_2;
	return (ret);
}