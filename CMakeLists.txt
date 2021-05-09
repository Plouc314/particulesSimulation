cmake_minimum_required(VERSION 3.4...3.18)
project(PhySimulation)

find_package(pybind11 REQUIRED)

include_directories("${PROJECT_SOURCE_DIR}")

include_directories(
        ${PROJECT_SOURCE_DIR}/include
        ${PROJECT_SOURCE_DIR}/src
)

file(GLOB all_SRCS
	"${PROJECT_SOURCE_DIR}/include/*.hpp"
        "${PROJECT_SOURCE_DIR}/src/*.cpp"
        )

pybind11_add_module(cppSimulation ${all_SRCS})
