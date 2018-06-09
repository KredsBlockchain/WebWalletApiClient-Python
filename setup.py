from setuptools import setup,find_packages

setup(
	name = "kredswallet",
	version = "0.1",
	install_requires = ["base64","time","requests","hashlib","json"],
	author = "MustyMouse",
	author_email = "admin@krux.us",
	description = ("A Python wrapper for the Kredswallet Web API"),
	license = "GNU",
	keywords = "kredswallet python wrapper",
	url = "https://github.com/MustyMouse/kredswallet",
	packages = find_packages(exclude=["docs","tests"]),
	classifiers = [
		"Development Status :: 3 - Alpha",
		"License :: OSI Approved :: GNU General Public License (GPL)",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.6"
	],
)
