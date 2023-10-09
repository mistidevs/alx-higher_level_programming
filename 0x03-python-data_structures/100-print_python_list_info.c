#include <time.h>
#include <Python.h>
#include <stdio.h>

/**
* print_python_list_info - writing CPython code to analyse Python code
* @p: a pointer to a PyObject
*
* Return: void
*/

void print_python_list_info(PyObject *p)
{
Py_ssize_t len, allocated, i;
PyObject *item;

len = PyList_Size(p);
allocated = ((PyListObject *)p)->allocated;
printf("[*] Size of the Python List = %ld\n", len);
printf("[*] Allocated = %ld\n", allocated);

for(i = 0; i < len; i++)
{
	item = PyList_GetItem(p, i);
	printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
}
}
