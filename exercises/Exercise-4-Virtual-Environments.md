## Exercise 4: Virtual Environments

#### Goal

Create a virtual environment + (editable) install your package + see that your dependencies are automatically installed

#### Tasks

We will use `venv` as our environment manager - it is a basic one, but all the principles will apply to all other package managers as well.

  * Check which Python you are currently using, and which packages are installed. Uninstall the brewing package and check that it is not there anymore.
  * Navigate to the folder which contains the brewing package
  * Create and activate a new environment
  * Check again which Python you are using and which packages are installed - Are they different?
  * Make an editable installation of the `brewing` package and check that the code still works

#### Commands in case you get stuck (not in correct order):

```bash
> which python
> pip freeze
> pip uninstall brewing
> pip install -e <path-to-folder-containing-brewing>


# create an environment option 1 (environment lives in the project folder)
> cd <path-to-project_folder>
> python -m venv .
> source ./bin/activate

# create an environment option 2 (environment lives in a central location)
> mkdir /home/student/envs/ 
> python3 -m venv /home/student/envs/brewing
> source /home/student/envs/brewing/bin/activate


# fyi: deactivate a venv environment
> deactivate
```
