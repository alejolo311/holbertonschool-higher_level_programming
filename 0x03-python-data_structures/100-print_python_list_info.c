#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints python list
 * @p: a pointer to a pyobj
 * Return: is a void func
 */
void print_python_list_info(PyObject *p)
{
	long int size, alloc, i;
        PyObject *item;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);

	}
}