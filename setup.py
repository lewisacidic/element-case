import sys
from setuptools import find_packages, setup, Command
from setuptools.command.test import test as TestCommand


class BlackCommand(Command):
    """ Command to format code with Black """

    user_options = [("black-args-", "a", "Arguments to pass to black")]

    def initialize_options(self):
        self.black_args = "."

    def finalize_options(self):
        pass

    def run(self):
        import black, shlex

        errno = black.main(shlex.split(self.black_args))


class PyTestCommand(TestCommand):
    """ Command to run tests using pytest """

    user_options = [("pytest-args-", "a", "Arguments to pass to pytest")]

    def initialize_options(self):
        super().initialize_options()
        self.pytest_args = ""

    def run_tests(self):
        import shlex, pytest

        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


setup(
    name="element-case",
    version="1.0",
    description="Element Case writing capabilities",
    author="Rich Lewis",
    author_email="richlewis42@users.noreply.github.com",
    project_urls={
        "bugs": "https://github.com/richlewis42/element-case/issues",
        "source": "https://github.com/richlewis42/element-case",
    },
    packages=find_packages(),
    license="MIT",
    tests_require=["pytest"],
    cmdclass={"test": PyTestCommand, "format": BlackCommand},
)
