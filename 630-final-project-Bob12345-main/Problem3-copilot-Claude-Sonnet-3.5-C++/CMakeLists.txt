cmake_minimum_required(VERSION 3.10)
project(MedianSortedArrays)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find nlohmann_json package
find_package(nlohmann_json 3.2.0 REQUIRED)

# Add executable
add_executable(run_tests run_tests.cpp)

# Link against nlohmann_json
target_link_libraries(run_tests PRIVATE nlohmann_json::nlohmann_json)