#include <Python.h>

void print_python_bytes(PyObject *p);

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
	printf("Elemetn %ld: %s\n", i, item->ob_type->tp_name);
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
long int size, i;
char *trying_str;
unsigned char *bytes_str;

printf("[.] bytes object info\n");

if (!PyBytes_Check(p))
{
	printf("  [ERROR] Invalid Bytes Object\n");
	return;
}

size = ((PyVarObject *)p)->ob_size;
trying_str = ((PyBytesObject *)p)->ob_sval;

printf("  size: %ld\n", size);
printf("  trying string: %s\n", trying_str);

if (size < 10)
	printf("  first %ld bytes:", size + 1);
else
	printf("  first 10 bytes:");

bytes_str = (unsigned char *)trying_str;
for (i = 0; i < size && i < 10; i++)
	printf(" %02hhx", bytes_str[i]);

printf("\n");
}
