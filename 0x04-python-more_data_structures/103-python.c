#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
* print_python_list - printing a PyObject List
* @p: pointer to PyObject
*
* Return: void
*/

void print_python_list(PyObject *p)
{
long int size, i;
PyObject *item;

printf("[*] Python list info\n");

if (!PyList_Check(p))
{
	printf("  [ERROR] Invalid List Object\n");
	return;
}

size = ((PyVarObject *)p)->ob_size;
printf("[*] Size of Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
	item = *((PyObject **)(((PyListObject *)p)->ob_item) + i);
	printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	if (PyBytes_Check(item))
		print_python_bytes(item);
}
}


/**
* print_python_bytes - printing Bytes object bytes
* @p: pointer to PyObject
*
* Return: void
*/

void print_python_bytes(PyObject *p)
{
long int size, i, len;
char *str;

printf("[.] bytes object info\n");

if (!PyBytes_Check(p))
{
	printf("  [ERROR] Invalid Bytes Object\n");
	return;
}

size = ((PyVarObject *)p)->ob_size;
str = ((PyBytesObject *)p)->ob_sval;
len = size + 1 > 10 ? 10 : size + 1;
printf("  size: %ld\n", size);
printf("  trying string: %s\n", str);
printf("  first %lu bytes: ", len);

for (i = 0; i < len; i++)
	printf(" %02hhx%s", str[i], i + 1 < len ? " " : "");
printf("\n");
}
