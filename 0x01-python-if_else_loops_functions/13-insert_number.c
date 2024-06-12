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

	if (head == NULL)
		return (NULL);
	insertnode = (listint_t *)malloc(sizeof(listint_t));
	if (insertnode == NULL)
		return (NULL);
	insertnode->n = number;
	insertnode->next = NULL;
	if (*head == NULL || (*head)->n >= number)
	{
		insertnode->next = *head;
		*head = insertnode;
		return (insertnode);
	}
	temp = *head;
	while (temp->next != NULL && temp->next->n < number)
	{
		temp = temp->next;
	}
	insertnode->next = temp->next;
	temp->next = insertnode;
	return (insertnode);
}
