# flx

[![Build Status](https://travis-ci.org/steenzout/flx.svg?branch=master)](https://travis-ci.org/steenzout/flx)
[![Code Health](https://landscape.io/github/steenzout/flx/master/landscape.png)](https://landscape.io/github/steenzout/flx/master)
[![Requirements Status](https://requires.io/github/steenzout/flx/requirements.png?branch=master)](https://requires.io/github/steenzout/flx/requirements/?branch=master)

This product is licensed under the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0).


## flx

This is the directory which will hold the flx source code.


## docs

Directory where you'll store the [Sphinx](http://sphinx-doc.org) configuration files and
where the documentation will be generated.


## .gitignore

File where you specify which files [Git](http://en.wikipedia.org/wiki/Git_(software)) should ignore.

A generic file has been provided.

You can use [gitignore.io](http://www.gitignore.io) to
produce other files that will better suit your development environment.

For more information, you can check "[git-scm.com : gitignore](http://git-scm.com/docs/gitignore)".


## LICENSE

The Apache 2 license.


## pytest.ini

The [pytest](https://pytest.org/latest/index.html) configuration file.

You can read
"[pytest : Changing standard (Python) test discovery](https://pytest.org/latest/example/pythoncollection.html)"
for more information on how to use this file to customize [pytest](https://pytest.org/latest/index.html)'s behavior.


## README.md

This file.

Check "[here](http://daringfireball.net/projects/markdown/syntax)" for help
with [Markdown](http://daringfireball.net/projects/markdown/) syntax.


## requirements.txt

On this file you specify the list of packages the project depends.

Read "[pip : Requirement Files](http://www.pip-installer.org/en/latest/user_guide.html#requirements-files)"
to understand how you can properly use this file to define your project's dependencies.


## setup.py

The setup script whre you'll describe the project / product, authors, maintainers and
information on how to distribute it.

Read "[Python : 2. Writing the Setup Script](http://docs.python.org/2/distutils/setupscript.html)",
for more information.


## tests

The directory where the unit tests reside.


## test-requirements.txt

On this file you specify the list of packages the project needs to run its tests.

An example of the possible contents of this file has been provided.

Read "[pip : Requirement Files](http://www.pip-installer.org/en/latest/user_guide.html#requirements-files)"
to understand how you can properly use this file to define your project's test dependencies.


# tox.ini

The [tox](http://tox.readthedocs.org/en/latest/) configuration file.

It contains basic information about your project and test environments.

I recommend [installling tox](http://tox.readthedocs.org/en/latest/install.html) and
use it to run your tests and generate the documentation.

```
# run the tests
$ tox

# generate the documentation
$ tox -e docs
```
