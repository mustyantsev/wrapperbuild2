from conans import ConanFile, CMake

class clientCsharpConan(ConanFile):
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"

    def requirements(self):
        self.requires("opentdf-client/2.0.0@")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
