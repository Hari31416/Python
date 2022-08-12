users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")


# working with list of dictionary
dragon = {
    'first' : 'rand',
    'last' : 'althor',
    'gender' : 'male',
    'age' : '19',
    'city' : 'two rivers',
    }
shallan = {
    'first' : 'shallan',
    'last' : 'devar',
    'gender' : 'female',
    'age' : '20',
    'city' : 'alethar'
    }
peoples = [dragon, shallan]
for people in peoples:
    name = f"{people['first']} {people['last']}"
    print(f"\nName: {name.title()}")
    for key, value in people.items():
        if key != 'first' and key != 'last':
            print(f"{key.title()} : {value.title()}")
    