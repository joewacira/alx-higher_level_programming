#include "lists.h"

/**
 * get_dnodeint_at_index - func returns nth node of dlistint_t linked list.
 * @head: the pointer to head of a list
 * @index: the index of node to search, begining from 0
 * Return: nth node else (null)
 **/
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int size;
	dlistint_t *tmp;

	size = 0;
	if (head == NULL)
	return (NULL);

	tmp = head;
	while (tmp)
	{
	if (index == size)
	return (tmp);
	size++;
	tmp = tmp->next;
	}
	return (NULL);
}
