# fmtlib Conan package
# Dmitriy Vetutnev, ODANT 2020


from conans import ConanFile, CMake, tools
import os


class GoogletestConan(ConanFile):
    name = "fmt"
    version = "11.0.2+0"
    license = "https://raw.githubusercontent.com/fmtlib/fmt/master/LICENSE.rst"
    description = "{fmt} is an open-source formatting library for C++. It can be used as a safe and fast alternative to (s)printf and iostreams."
    url = "https://github.com/odant/conan-fmt"
    settings = {
        "os": ["Windows", "Linux"],
        "compiler": ["Visual Studio", "gcc"],
        "build_type": ["Debug", "Release"],
        "arch": ["x86", "x86_64", "mips", "armv7"]
    }
    options = {
        "with_unit_tests": [True, False],
        "ninja": [True, False]
    }
    default_options = {
        "with_unit_tests": False,
        "ninja": True
    }
    generators = "cmake"
    exports_sources = "src/*", "CMakeLists.txt"
    no_copy_source = True
    build_policy = "missing"

    def build_requirements(self):
        if self.options.ninja:
            self.build_requires("ninja/[>=1.9.0]")

    def build(self):
        cmake = CMake(self, msbuild_verbosity='normal')
        cmake.verbose = True
        cmake.definitions["FMT_INSTALL"] = "ON"
        cmake.definitions["FMT_DOC"] = "OFF"
        if self.options.with_unit_tests:
            cmake.definitions["FMT_TEST"] = "ON"
        if self.settings.get_safe("compiler.runtime") in ("MT", "MTd"):
            cmake.definitions["MSVC_BUILD_STATIC"] = "ON"
        cmake.configure()
        cmake.build()
        if self.options.with_unit_tests:
            if cmake.is_multi_configuration:
                self.run("ctest --output-on-failure --build-config %s" % build_type)
            else:
                self.run("ctest --output-on-failure")
        cmake.install()
        tools.rmdir(os.path.join(self.package_folder, "lib/pkgconfig"))

    def package(self):
        self.copy("*fmt.pdb", dst="bin", keep_path=False)

    def package_id(self):
        self.info.options.with_unit_tests = "any"
        self.info.options.ninja = "any"

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

