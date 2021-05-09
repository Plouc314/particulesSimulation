# include <pybind11/pybind11.h>
# include <pybind11/stl.h>
# include <vector>
# include "system.hpp"
# include "partcule.hpp"
# include "physic.hpp"

namespace py = pybind11;

std::vector<float> to_list(const Vect2D<float> &vect) {
    std::vector<float> list = {vect.x, vect.y};
    return list;
}

PYBIND11_MODULE(cppSimulation, m) {
    m.doc() = "Physical simulation";

    py::class_<Constants>(
        m, "Constants"
    ).def(py::init<>())
    .def_property("k", &Constants::getK, &Constants::setK)
    .def_property("e", &Constants::getE, &Constants::setE)
    .def_readonly("masse_proton", &Constants::masseProton) 
    .def_readonly("masse_neutron", &Constants::masseNeutron) 
    .def_readonly("masse_electron", &Constants::masseElectron) 
    .def_readonly("charge_proton", &Constants::chargeProton) 
    .def_readonly("charge_electron", &Constants::chargeElectron) 
    ;

    py::class_<Particule>(
        m, "Particule"
    )
    .def(py::init<float, float, float, float>())
    .def_readwrite("q", &Particule::q)
    .def_property("pos", &Particule::getListPos, &Particule::setListPos)
    .def_property("v", &Particule::getListV, &Particule::setListV)
    .def_property("a", &Particule::getListA, &Particule::setListA)
    ;

    py::class_<System>(
        m, "System"
    )
    .def(py::init<std::vector<Particule>&, float>(), py::arg("particules"), py::arg("dt") = -1)
    .def_readonly("particules", &System::particules)
    .def_property_readonly("constants", &System::constants)
    .def("update", &System::updateState, py::arg("dt") = -1, "Update the simulation state.")
    .def("print", &System::print)
    ;
}