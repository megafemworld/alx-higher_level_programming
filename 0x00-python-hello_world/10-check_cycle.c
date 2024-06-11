#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle.
 * @list: the list to check.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t temp;

	if (list == NULL)
		return (0);
	temp = (*list)->next;
	while (temp != NULL)
	{
		if (temp == *list)
		{
			return (1);
		}
	}
	return (0);
}
