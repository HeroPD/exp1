#include <pybind11/pybind11.h>

namespace py = pybind11;

int add(int i, int j) {
    return i + j;
}

PYBIND11_MODULE(core, m) {
    m.def("add", &add, "A function that adds two numbers");
}
