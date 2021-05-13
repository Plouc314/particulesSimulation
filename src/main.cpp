# include <pybind11/pybind11.h>
# include <pybind11/stl.h>
# include <vector>
# include "system.hpp"
# include "partcule.hpp"
# include "physic.hpp"

namespace py = pybind11;

PYBIND11_MODULE(_simulation, m) {

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

    py::class_<MagneticField>(
        m, "MagneticField"
    )
    .def(py::init<float, float, float, float, bool>(), py::arg("x"), py::arg("y"), py::arg("intensity"), py::arg("dispersion") = -1, py::arg("isUniform") = true)
    .def_readwrite("intensity", &MagneticField::intensity)
    .def_readwrite("dispersion", &MagneticField::dispersion)
    .def_readwrite("is_uniform", &MagneticField::isUniform)
    .def_property_readonly("origin", &MagneticField::getListOrigin)
    ;

    py::class_<System>(
        m, "System"
    )
    .def(py::init<std::vector<Particule>&, float>(), py::arg("particules"), py::arg("dt") = -1)
    .def_readonly("particules", &System::particules)
    .def_readonly("magnetic_fields", &System::magneticFields)
    .def_property_readonly("constants", &System::constants)
    .def_property_readonly("n_particules", &System::getNumberParticules)
    .def("set_limits", &System::setLimits)
    .def("update", &System::updateState, py::arg("dt") = -1, "Update the simulation state.")
    .def("clear_elements", &System::clearElements)
    .def("add_particule", &System::addParticule)
    .def("add_magnetic_field", &System::addMagneticField)
    .def("print", &System::print)
    ;
}