#include "lists.h"

/**
 * check_cycle - checks to see if a list is in an endless loop or cycle
 * list: the list to check
 * Return: 0 if no cycle is detected, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *reg, *doub;

	reg = list;
	doub = list;

	while (reg != NULL && doub != NULL)
	{
		reg = reg->next;
		doub = doub->next->next;

		if (reg == doub)
			return (1);

	}
	return (0);
}
