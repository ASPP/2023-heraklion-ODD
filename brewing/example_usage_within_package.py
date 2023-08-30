# Task: import make_example_potion from the module brew_potions.py
import brew_potions
brew_potions.make_example_potion("student")

from brew_potions import make_example_potion
make_example_potion("student")

import brew_potions as br
br.make_example_potion("student")
