## Exercise 2: Editable Installation

#### Goal

See advantages of using brewing package as an editable installation.

#### Tasks

1. check which packages are installed currently with the command `pip freeze`

2. install the brewing package as an editable installation ➔ in the terminal, change to the tp level directory where you cloned the repo and perform an editable installation of the package
   with the command `pip install -e .`

3. check which packages are installed now with `pip freeze` ➔ what changed?

4. Try running the `example_usage_X.py` files that you created in Exercise 1. Do they run without errors and if no, can you make them all work simultaneously?
   * [`example_usage_outside_package.py`](../example_usage_outside_package.py)
   * [`scripts/example_usage_different_folder.py`](../scripts_and_notebooks/example_usage_outside_package.py)
   * [`brewing/example_usage_within_package.py`](../brewing/example_usage_within_package.py)
   * (Hint: use abolute imports ➔ now `brewing` is installed as a package!)
