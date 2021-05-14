#3.4
guests = ['rand', 'perrin', 'mat', 'nightblood']
print(f"Hello, {guests[0].title()}! Would you like to have dinner? Don't worry there is no box here!")
print(f"{guests[1].title()}! Would you like to have dinner? And {guests[1].title()}, please bring the axe.")
print(f"Hello, {guests[2].title()}! Would you like to have dinner?")
print(f"Hello, {guests[3].title()}! Would you like to kill some evil tonight?")

#3.5
print(guests[2].title())
guests[2] = "kal"
print(guests)
print(f"Hello, {guests[0].title()}! Would you like to have dinner? Don't worry there is no box here!")
print(f"{guests[1].title()}! Would you like to have dinner? And {guests[1].title()}, please bring the axe.")
print(f"Hello, {guests[2].title()}! Would you like to have dinner?")
print(f"Hello, {guests[3].title()}! Would you like to kill some evil tonight?")

#3.6
print("I found a bigger dinner table!")
guests.insert(0, 'shallan')
guests.insert(3, 'vin')
guests.append('denna')
print(f"Hello, {guests[0].title()}! Wanna make some sketch?")
print(f"Hello, {guests[1].title()}! Would you like to have dinner? Don't worry there is no box here!")
print(f"{guests[2].title()}! Would you like to have dinner? And {guests[2].title()}, please bring the axe.")
print(f"Hello, {guests[3].title()}! I have some atium!")
print(f"Hello, {guests[4].title()}! Would you like to have dinner?")
print(f"Hello, {guests[5].title()}! Would you like to kill some evil tonight?")
print(f"{guests[6].title()}, would you like to have dinner? Haha, seven words!")
print(guests)

#3.7
print("Oops! I can invite only two people for dinner now!")
guest_1 = guests.pop()
print(f"Sorry, {guest_1.title()} I can not give you dinner anymore.")
guest_2 = guests.pop()
print(f"Sorry, {guest_2.title()} I can not give you dinner anymore.")
guest_3 = guests.pop()
print(f"Sorry, {guest_3.title()} I can not give you dinner anymore.")
guest_4 = guests.pop()
print(f"Sorry, {guest_4.title()} I can not give you dinner anymore.")
print(guests)
del guests[2]
del guests[1]
del guests[0]
print(guests)