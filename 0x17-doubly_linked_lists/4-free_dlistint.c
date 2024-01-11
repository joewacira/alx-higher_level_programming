#include "lists.h"

/**
 * free_dlistint - the func frees dlistint_t list.
 * @head: the pointer to head of a list
 * Return: null
 **/
void free_dlistint(dlistint_t *head)
{
	if (head == NULL)
	return;

	while (head->next)
	{
	head = head->next;
	free(head->prev);
	}
	free(head);
}
