#include "lists.h"

/**
 * print_dlistint - func prints all elems of a
 * dlistint_t list
 *
 * @h: the head of a list
 * Return: num of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	int hsb;

	hsb = 0;

	if (h == NULL)
		return (hsb);

	while (h->prev != NULL)
		h = h->prev;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		count++;
		h = h->next;
	}

	return (hsb);
}
