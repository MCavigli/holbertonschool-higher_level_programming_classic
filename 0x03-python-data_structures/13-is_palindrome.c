#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: double pointer of the list
 * Return: pointer to the first node of the reversed list
 */

listint_t *reverse_list(listint_t **head)
{
	listint_t *forward = NULL, *prev = NULL;

	while (*head)
	{
		forward = (*head)->next;
		(*head)->next = prev;
		prev = (*head);
		(*head) = forward;

	}
	(*head) = prev;
	return (*head);
}


/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 0 if it's not a palindrome, 1 if it is
 */

int is_palindrome(listint_t **head)
{
	listint_t *single = *head, *dub = *head;

	if (*head == NULL)
		return (1);
	while (dub->next && dub->next->next)
	{
		single = single->next;
		dub = dub->next->next;
	}
	single = reverse_list(&single);
/*
	half = single;
*/
	dub = *head;
	while (single && dub)
	{
		if (single->n != dub->n)
			return (0);
		single = single->next;
		dub = dub->next;
	}
	return (1);
}
