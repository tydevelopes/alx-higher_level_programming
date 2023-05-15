#include "lists.h"

int listint_len(const listint_t *h);
void copy_list_values(const listint_t *h, int arr[]);
int is_palindrome_helper(int arr[], int i, int j);

/**
 * is_palindrome - inserts a new node in a sorted list
 * @head: pointer to head pointer to the list
 * Return: 1 if palindrom, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int list_len = listint_len(*head);
	int arr[list_len];

	if (!*head)
		return (1);

	copy_list_values(*head, arr);
	return (is_palindrome_helper(arr, 0, list_len - 1));
}

/**
 * listint_len - returns the number of elements in a linked listint_t list
 * @h: pointer to the list
 * Return: number of elements in the list
 */
int listint_len(const listint_t *h)
{
	int length = 0;
	const listint_t *current_node = NULL;

	if (!h)
		return (length);
	current_node = h;
	while (current_node)
	{
		length++;
		current_node = current_node->next;
	}
	return (length);
}
/**
 * copy_list_values - copy list into array
 * @h: pointer to the list
 * @arr: array to store int values from list
 */
void copy_list_values(const listint_t *h, int arr[])
{
	int i = 0;
	const listint_t *current_node = NULL;

	if (!h)
		return;
	current_node = h;
	while (current_node)
	{
		arr[i] = current_node->n;
		i++;
		current_node = current_node->next;
	}
}

/**
 * is_palindrome_helper - recursively checks if a string is palindrome
 * @arr: array to check
 * @i: current position at the beginning of the string
 * @j: current position at end of the string
 * Return: returns 1 if palindrome, 0 otherwise
 */
int is_palindrome_helper(int arr[], int i, int j)
{
	if (i >= j)
		return (1);
	if (arr[i] != arr[j])
		return (0);
	return (is_palindrome_helper(arr, i + 1, j - 1));
}
