#include "lists.h"

/**
 * check_cycle - evaluates if a linked list has a cycle
 * @list: list to be evaluated
 * Return: 1 if cycle is present else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (!list)
		return (0);
	while (slow && fast && fast -> next)
	{
		slow = slow -> next;
		fast = fast -> next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
