# Define ages based on relationships
Anton_age = 21
Beth_age = Anton_age + 6
Chen_age = Beth_age + 20
Drew_age = Chen_age + Anton_age
Ethan_age = Chen_age

def main():
    print(f""" 
    AGES
    Anton is {Anton_age}
    Beth is {Beth_age}
    Chen is {Chen_age}
    Drew is {Drew_age}
    Ethan is {Ethan_age}
""")

if __name__ == '__main__':
    main()
