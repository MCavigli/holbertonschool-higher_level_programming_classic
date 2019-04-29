#include "lists.h"

/**
 * check_cycle - checks to see if a list is in an endless loop or cycle
 * @list: the list to check
 * Return: 0 if no cycle is detected, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *doub = list;

	while (list != NULL && doub != NULL)
	{
		list = list->next;
		doub = doub->next->next;

		if (list == doub)
			return (1);

	}
	return (0);
}
