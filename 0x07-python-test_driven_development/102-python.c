#include <Python.h>


void print_python_string(PyObject *p)
{
Py_ssize_t len;
const char *str;
const char *type;

printf("[.] string object info\n");

if(!PyUnicode_Check(p))
{
	printf("  [ERROR] Invalid String Object\n");
	return;
}

if (PyUnicode_IS_COMPACT_ASCII(p))
	type = "compact ascii";
else
	type = "compact unicode object";

str = PyUnicode_AsUTF8AndSize(p, &len);

printf("  type: %s\n", type);
printf("  length: %ld\n", len);
printf("  value: %s\n", str);
}
