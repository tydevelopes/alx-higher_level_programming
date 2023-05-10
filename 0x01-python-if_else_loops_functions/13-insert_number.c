#include "lists.h"

/**
 * insert_node - inserts a new node in a sorted list
 * @head: pointer to head pointer to the list
 * @number: number to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = *head;
	listint_t *previous_node = NULL;
	listint_t *temp = NULL;
	unsigned int current_index = 0;

	if (!head)
		return (NULL);

	temp = malloc(sizeof(listint_t));
	if (!temp)
		return (NULL);
	temp->n = number;
	temp->next = NULL;

	while (current_node && number > current_node->n)
	{
		previous_node = current_node;
		current_node = current_node->next;
		current_index++;
	}
	if (!current_node && current_index == 0)
		*head = temp;
	else if (!previous_node && current_index == 0)
	{
		temp->next = current_node;
		*head = temp;
	}
	else if (current_index != 0)
	{
		previous_node->next = temp;
		temp->next = current_node;
	}
	else
	{
		free(temp);
		temp = NULL;
	}
	return (temp);
}
