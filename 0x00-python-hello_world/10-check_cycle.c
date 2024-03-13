#include "lists.h"
/**
*check_cycle - checks if list is cycled
*@list: points to list
*Return: int
**/
int check_cycle(listint_t *list)
{
listint_t *temp = NULL;
temp = list;
if (!temp)
	return (0);
while (temp)
{
temp = temp->next;
if (temp == NULL)
	return (1);
else if (temp == list)
	return (0);
}
return (0);
}
