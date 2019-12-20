#include <object.h>
#include <string.h>
#include <Python.h>
#include <listobject.h>



/**
 * print_python_list - print basic python lsits
 * @p: pyobject
 * Return: void
 */
void print_python_list(PyObject *p)
{
	int i, s, a;
	char *dataType;
	PyListObject *l:


    l = (PyListObject *)p, s = PyList_Size(p), a = l->a;
    printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %i\n", s);
	printf("[*] Allocated = %i\n", a);
	for (i = 0; i < s; i++)
	{
		dataType = (l->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, dataType);
		strcmp(dataType, "bytes") == 0 ? print_python_bytes(l->ob_item[i]) : l;
	}
}

/**
 * print_python_bytes - print basic shit about python
 * byte objects
 * @p: pointer to PyObject p
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
    char *str;
	int i;
	ssize_t b;


	printf("[.] b object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytes_AsStringAndSize(p, &str, &b);
	printf("  size: %li\n", b), printf("  trying string: %s\n", str);
	b > 10 ? b = 10 : b++;
	printf("  first %li bytes: ", b);
	for (i = 0; i < b - 1; i++)
		printf("%02hhx ", str[i]);
	printf("%02hhx", str[i]);
	printf("\n");
}
