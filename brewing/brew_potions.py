from brewing import potion_class
from brewing import containers
from brewing import cooking
from brewing import inspection


def make_example_potion(student_name="ASPP student"):
    my_potion = potion_class.Potion(student_name=student_name)
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=containers.old_kettle, heat_source=cooking.eternal_flame)
    # Simmer for 5 hours.
    cooking.simmer(my_potion, duration=5)
    print(f"You successfully ran make_example_potion, {student_name}, well done :).")
    return my_potion


def make_python_expert_potion(student_name):
    """"
    Takes a string indicating the name of a student and returns a "Potion" object.

    The function sets the following properties of the Potion object: 
        - container
        - heat_source
        - ingredients
        - simmer_duration
    according to the "python_expert" target_portion specification for 
    brewing.inspection.inspection_by_Snape()

    """
    print("I am a Python Expert")
    # todo: write this function!
    my_potion = potion_class.Potion(student_name=student_name)
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=containers.pewter_cauldron, heat_source=cooking.fire)
    my_potion.add_ingredients(ingredients=['fish_eyes','tea_leaves','unicorn_hair'])
    cooking.simmer(my_potion, duration=2)
    return my_potion


if __name__ == "__main__":
    my_name = 'ASPP student'
    my_potion = make_python_expert_potion(student_name=my_name)
    # Let Snape inspect the potion
    inspection.inspection_by_Snape(potion=my_potion, target_potion='python_expert')
