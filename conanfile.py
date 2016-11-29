from conans import ConanFile
from conans.tools import download, check_sha256

class NodConan(ConanFile):
    name = "nod"
    version = "0.3.4"
    settings = "os", "compiler", "build_type", "arch"
    url = "https://github.com/fr00b0/conan-nod"
    license = "MIT"

    header_file = "nod.hpp"
    download_url = "https://raw.githubusercontent.com/fr00b0/nod/74097db0c8e7bbc9807b5ab0c0b527364e1774b1/include/nod/nod.hpp"
    sha256_hash = "324f6f6dff45395120e27331a8d6ca5090337e230049a7f2bf0405e5753c0247"

    def source(self):
        download(self.download_url, self.header_file)
        check_sha256(self.header_file, self.sha256_hash)

    def build(self):
        pass  # Header only library

    def package(self):
        self.copy(self.header_file, dst="include/nod", src=".")

    def package_info(self):
        pass  # Header only library
