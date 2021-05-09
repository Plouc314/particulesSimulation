#!/usr/bin/bash

cd build
cmake ..
make
mv cppSimulation.cpython-38-x86_64-linux-gnu.so ../python/lib/simulation
cd ../python
echo Running tests...
python3 tests.py -v