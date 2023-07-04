## Exercise 1: Importing

#### Goal

Get comfortable with different ways of importing objects from a package.

#### Preparation

0. [if not done already] fork the repository

    https://github.com/ASPP/2023-heraklion-ODD

   and clone it to the laptop in a new directory

1. You will be editing files within this directory
2. Open a terminal and change to this directory, so that you can run the scripts that you are editing

#### Tasks

1. Work on the file [`example_usage_within_package.py`](../brewing/example_usage_within_package.py) in the `brewing` directory:

   * import the module [`brew_potions.py`](../brewing/brew_potions.py) in the script ➔ open a terminal, change to the `brewing` directory and run the script [`example_usage_within_package.py`](../brewing/example_usage_within_package.py): what happens? 
   * import and call the `make_example_potion` function from the module [`brew_potions.py`](../brewing/brew_potions.py) in the script ➔ what happens when you run the script?
   * change the import statement so that you can call the `make_example_potion` function like this: `br.make_example_potion` ➔ run the script again: what happens?

2. Work on the file [`example_usage_outside_package.py`](../example_usage_outside_package.py), which is in the top level directory where you cloned the repo:
   * import `brewing` in the script ➔ in the terminal, change to the top level directory of the repo and run the script: what happens?
   * import and call only the `make_example_potion` function from the module [`brew_potions.py`](../brewing/brew_potions.py) ➔ run the script again: what happens?
   * does it work? if it doesn't work, what do you have to do to make it work?

3. Work on the file [`scripts_and_notebooks/example_usage_different_folder.py`](../scripts_and_notebooks/example_usage_different_folder.py), which is in the `scripts_and_notebooks` directory:
   * import `brewing` in the script ➔ in the terminal, change to the `scripts_and_notebooks` directory and run the script: what happens?
   * does it work? if it doesn't, what do you have to do to make it work? 
   * if you could fix the error above, try now to import and call only the `make_example_potion` function afrom the module [`brew_potions.py`](../brewing/brew_potions.py) ➔ run the script: what happens?
   * does it work? if it doesn't work, what do you have to do to make it work?
