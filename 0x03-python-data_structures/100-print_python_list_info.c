#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - prints python list
 * @p: a pointer to a pyobj
 * Return: is a void func
 */
void print_python_list_info(PyObject *p)
{
	long int i, len;
	PyListObject *obj;

    len = PyList_Size(p);
    PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < len; i++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
	}
}