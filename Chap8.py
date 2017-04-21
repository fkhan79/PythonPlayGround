#8-3
def createShirt(size, message):
    print("\nLets make a " +size + " t-shirt.")
    print('Shirt Title:, "' +message + '"')

createShirt('large', 'Anaconda!')
createShirt(message="Python and PyCharm, Deadly Combo.", size='medium')
createShirt(message="Python Rocks.", size='small')

#8-4
def createShirtWithDefaults(size='large', message='I love Python!'):
    print("\nLets make another Shirt with some default " +size + " t-shirt.")
    print('It will say, "' +message + '"')

createShirtWithDefaults()
createShirtWithDefaults(size='medium')
createShirtWithDefaults('small', 'Skinny Tigers.')

#8-5
def describe_city(city, country='chile'):
    msg =city.title() + " is in " +country.title() + "."
    print(msg)

describe_city('santiago')
describe_city('reykjavik', 'iceland')
describe_city(city="Karachi",country="Pakistan")

#8-12
def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nSandwich Time:")
    for item in items: print(" adding " +item + " to your sandwich.")
    print("Your sandwich is ready!\n")

make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey mustard')
make_sandwich('turkey bacon', 'sour dills', 'honey mustard')
make_sandwich('butter', 'marmalade')

#8-13
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',location='princeton',field='physics',famousFor="E=MC^2")
print(user_profile)

#8-14
def build_car(name,type,**package):
    car = {}
    car['name'] = name
    car['type'] = type
    for key, value in package.items():
        car[key] = value

    return car
car = build_car('Honda Accura', 'Sedan',color='black',turbo='yes',wheelbase="16 Alloy")
print(car)

#8-15
import print_models as pf

unprinted_designs =['iphone case', 'robot pendant', 'dodecahedron']
completed_models =[]
pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)


#8-16
import Chap3
from Chap3 import invitations
guests = ['Ahmed', 'Rehan', 'Zeeshan']
print("Number of Guests invited: "+str(len(guests)))
invitations(guests)