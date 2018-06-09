from setuptools import setup,find_packages

setup(
	name = "kredswallet",
	version = "0.1a",
	install_requires = ["requests"],
	author = "MustyMouse",
	author_email = "admin@krux.us",
	description = ("A Python wrapper for the Kredswallet Web API"),
	license = "GNU",
	keywords = "kredswallet python wrapper",
	url = "https://github.com/MustyMouse/kredswallet",
	download_url = "https://github.com/MustyMouse/kredswallet/archive/0.1a.tar.gz",
	packages = find_packages(exclude=["docs","tests"]),
	classifiers = [
		"Development Status :: 3 - Alpha",
		"License :: OSI Approved :: GNU General Public License (GPL)",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.6"
	],
)
