# Introduction to Unit Testing with Python and GitHub

This repository accompanies the Oxford RSE online course delivered on 17 Feb 2021.

## Getting started

Before starting, make sure that you:

- have a [GitHub](http://github.com/) account, and are logged in
- have [Git](https://git-scm.com/) installed on your computer
- have [Python](https://www.python.org/downloads/) installed on your computer, v3.5 or newer

If you already have Python installed on your computer, you can check which version you have by opening a terminal (on macOS or Linux) or a command prompt (on Windows) and typing

```
python --version
```

If you install Python for this course, go to the link above and choose the default option for your operating system.
If you install Python on Windows, make sure you click the "add to path" option during installation.

## Use this repository as a template

Click the "Use this template" button on this page.
Give it a name, but otherwise leave the defaults as they are.

On your computer, clone the repository you have just imported:
- Click the green Code button at the top of the page
- Select HTTPS and copy the text provided
- From a terminal (on macOS or Linux) or a command prompt (on Windows), run
  ```
  git clone <paste-string-here>
  ```

## Create a virtual environment

From a terminal (on macOS or Linux) or a command prompt (on Windows), change to the directory created by running the git command above.

We recommend creating a virtual environment for this course.
Type
```
python -m venv venv
```

On macOS or Linux, activate this environment by running
```
source venv/bin/activate
```

On Windows, activate this environment by running
```
venv\Scripts\activate.bat
```

## Install packages and check everything is working

Run the following commands:
```
pip install --upgrade pip setuptools wheel
pip install -e .
```

You should see a message that ends with `Successfully installed <list of packages>`.

Then run:
```
pytest -v
```

You should see a message that ends with
```
tests/test_models.py::test_everything_works PASSED     [100%]

===================== 1 passed in 0.08s ======================
```

If you see this, you're all set for the course!

# Credits

Some material and code used in this course is based on [Software Carpentry](https://software-carpentry.org/) courses.

Software Carpentry material is [made available](https://software-carpentry.org/license/) under the [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/legalcode), and example code under the [MIT license](https://opensource.org/licenses/MIT).
