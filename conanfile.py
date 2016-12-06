from conans import ConanFile
from conans.tools import download, check_sha256

class NodConan(ConanFile):
    name = "nod"
    version = "0.4.0"
    settings = "os", "compiler", "build_type", "arch"
    url = "https://github.com/fr00b0/conan-nod"
    license = "MIT"

    header_file = "nod.hpp"
    download_url = "https://raw.githubusercontent.com/fr00b0/nod/8d2bbc22df5777f9ca2b762ee9ca4ca7704852a3/include/nod/nod.hpp"
    sha256_hash = "e13ce4af80810c006b75fb0503db49e4489f5917c91f205d43125777ec137d13"

    def source(self):
        download(self.download_url, self.header_file)
        check_sha256(self.header_file, self.sha256_hash)

    def build(self):
        pass  # Header only library

    def package(self):
        self.copy(self.header_file, dst="include/nod", src=".")

    def package_info(self):
        pass  # Header only library
