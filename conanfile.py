from conans import ConanFile, tools, AutoToolsBuildEnvironment


class CppunitConan(ConanFile):
    name = "cppunit"
    version = "1.15"
    license = "LGPL2.1"
    author = "Guillem Castro guillemcastro4@gmail.com"
    url = "https://github.com/GuillemCastro/conan-cppunit"
    description = "CppUnit is the C++ port of the famous JUnit framework for unit testing."
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def source(self):
        self.run("git clone 'git://anongit.freedesktop.org/git/libreoffice/cppunit/'")

    def build(self):
        src_dir = "cppunit"
        autotools = AutoToolsBuildEnvironment(self)
        with tools.environment_append(autotools.vars):
            self.run("./autogen.sh", cwd=src_dir)
            self.run("./configure", cwd=src_dir)
            self.run("make", cwd=src_dir)

    def package(self):
        self.copy("*.h", dst="include", src="cppunit")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["cppunit"]