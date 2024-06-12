#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: head of the list.
 * @number: number to insert.
 *
 * Return: address of new node otherwise NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *insertnode;
	int hn = 0;

	if (*head == NULL || head == NULL)
		return (NULL);
	temp = *head;
	insertnode = (listint_t *)malloc(sizeof(listint_t));
	if (insertnode == NULL)
		return (NULL);
	while (temp != NULL)
	{
		if (number <= temp->n)
		{
			hn = 1;
			break;
		}
		if (temp->next != NULL)
		{
			if (number <= temp->next->n)
				break;
		}
		else
			break;
		temp = temp->next;
	}
	if ((*head) == temp && hn == 1)
	{
		insertnode->n = number;
		insertnode->next = *head;
		*head = insertnode;
		return (insertnode);
	}
	insertnode->n = number;
	insertnode->next = temp->next;
	temp->next = insertnode;
	return (insertnode);
}
