# Set the minimum version of CMake that's required
cmake_minimum_required(VERSION 3.12)

# Set the project name
project(DetDescr VERSION 2.1.0
                 DESCRIPTION "Detector description module."
                 LANGUAGES CXX
)

# Search and configure ROOT
find_package(ROOT 6.16 CONFIG REQUIRED)

setup_library(name DetDescr
              dependencies  ROOT::Core ROOT::Hist
                            Framework::Exception Framework::Configure 
)

# Setup the test
setup_test(dependencies DetDescr::DetDescr)

setup_python(package_name ${PYTHON_PACKAGE_NAME}/DetDescr)
