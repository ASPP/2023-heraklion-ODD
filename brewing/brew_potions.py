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
    print("I am a Python Expert")
    my_potion = potion_class.Potion(student_name=student_name)
    # Set up your pewter_cauldron and light a fire underneath it.
    my_potion.setup(container=containers.pewter_cauldron, heat_source=cooking.fire)
    # Add fish eyes, unicorn hair and tea leaves
    my_potion.add_ingredients(["fish_eyes", 'unicorn_hair', 'tea_leaves'])
    # Simmer for 2 hours.
    cooking.simmer(my_potion, duration=2)
    print(f"You successfully ran make_example_potion, {student_name}, well done :).")
    return my_potion


if __name__ == "__main__":
    my_name = 'E & H'
    my_potion = make_python_expert_potion(student_name=my_name)
    # Let Snape inspect the potion
    inspection.inspection_by_Snape(potion=my_potion, target_potion='python_expert')
