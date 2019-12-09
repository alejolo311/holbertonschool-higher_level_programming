#ifndef LISTS
#define LISTS

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer to store
 * @next: points to the struct
 *
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
int n;
struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);

#endif
