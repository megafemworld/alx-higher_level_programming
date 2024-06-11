#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle.
 * @list: the list to check.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL || list->next == NULL)
		return (0);
	slow = list;
	fast = list;
	while (slow != NULL && fast != NULL)
	{
		slow = slow->next;
		fast = fast->next;
		if (fast != NULL)
			fast = fast->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
