#include "lists.h"
/**
*check_cycle_recursive - checks if list is cycled
*@current: points to list
*@original: original head
*Return: int
**/

int check_cycle_recursive(listint_t *current, listint_t *original)
{
if (current == NULL)
{
return (0);
}
if (current == original)
{
return (1);
}
return (check_cycle_recursive(current->next, original));
}
/**
*check_cycle - checks if list is cycled
*@list: points to list
*Return: int
**/
int check_cycle(listint_t *list)
{
if (list == NULL)
{
return (0);
}
return (check_cycle_recursive(list->next, list));
}
