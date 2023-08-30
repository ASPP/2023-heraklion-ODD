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
    python_expert = potion_class.Potion(student_name=student_name)
    python_expert.setup(container=containers.pewter_cauldron, heat_source=cooking.fire)
    python_expert.add_ingredients(['fish_eyes', 'unicorn_hair', 'tea_leaves'])
    cooking.simmer(python_expert, duration=2)
    return python_expert


if __name__ == "__main__":
    my_name = 'ASPP student'
    python_expert = make_python_expert_potion(student_name=my_name)
    inspection.inspection_by_Snape(potion=python_expert, target_potion='python_expert')
