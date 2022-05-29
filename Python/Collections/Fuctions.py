def say_hello(*peoples):  # n1, n2, n3, n4

  for name in peoples:

    print(f"Hello {name}")

say_hello("Osama", "Ahmed", "Sayed", "Mahmoud")

# -- Function Default Parameters --
# ---------------------------------

def say_hello(name="Unknown", age="Unknown", country="Unknown"):

  print(f"Hello {name} Your Age is {age} and Your Country Is {country}")

say_hello("Osama", 36, "Egypt")
say_hello("Mahmoud", 28, "KSA")
say_hello("Sameh", 38)
say_hello("Ramy")
say_hello()

# ----------------------------------------------------
# -- Function Packing, Unpacking Arguments **KWArgs --

mySkills = {
  'Html': "80%",
  'Css': "70%",
  'Js': "50%",
  'Python': "80%",
  "Go": "40%"
}

def show_skills(**skills):

  print(type(skills))

  for skill, value in skills.items():

    print(f"{skill} => {value}")

show_skills(**mySkills)

# -----------------------------------------------------
# -- Function Packing, Unpacking Arguments Trainings --
# -----------------------------------------------------

myTuple = ("Html", "CSS", "JS")

mySkills = {
  'Go': "80%",
  'Python': "50%",
  'MySQL': "80%"
}

def show_skills(name, *skills, **skillsWithProgres):

  print(f"Hello {name} \nSkills Without Progress Is: ")

  for skill in skills:

    print(f"- {skill}")

  print("Skills With Progress Is: ")

  for skill_key, skill_value in skillsWithProgres.items():

    print(f"- {skill_key} => {skill_value}")

show_skills("Osama", *myTuple, **mySkills)

#_______Global scope
def var():
    global x
    x = 2
    print(x)

#x = 0
var()
print(x)

# Recursion Function.
def removeDouble(wrd):
    if len(wrd) == 1:
        return wrd
    if wrd[0] == wrd[1]:
        return removeDouble(wrd[1:])
    return wrd[0] + removeDouble(wrd[1:])

print(removeDouble('wwfffffffkkkkkccccc'))