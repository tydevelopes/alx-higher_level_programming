#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	const listint_t *node_ptr_A = head;
	const listint_t *node_ptr_B = head;

	if (!list || !list->next)
		return (0);

	while (node_ptr_B && node_ptr_B->next)
	{
		node_ptr_A = node_ptr_A->next;
		node_ptr_B = node_ptr_B->next->next;

		if (node_ptr_A == node_ptr_B)
			return (1);
	}

	return (0);
}
