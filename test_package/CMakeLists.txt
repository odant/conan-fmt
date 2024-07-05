project(PackageTest CXX)
cmake_minimum_required(VERSION 3.0)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

enable_testing()


# CONAN_PKG imported targets

add_compile_options(/permissive- /EHa /MP /utf-8 /W3 /Zc:__cplusplus /Zc:preprocessor)
add_executable(test_fmt_CONAN_PKG test_fmt.cpp)
target_link_libraries(test_fmt_CONAN_PKG CONAN_PKG::fmt)
add_test(
    NAME test_fmt_CONAN_PKG
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_fmt_CONAN_PKG
)


# fmt imported targets

find_package(fmt REQUIRED)

add_executable(test_fmt test_fmt.cpp)
target_link_libraries(test_fmt fmt::fmt)
add_test(
    NAME test_fmt
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_fmt
)

