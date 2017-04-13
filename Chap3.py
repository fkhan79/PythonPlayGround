def invitations(guests):
    txt = 'Hi %s:\nYou are invited to a dinner party at the beach\nHappy summers\n\n'
    for x in guests:
        print(txt % (x))
    return


# 3-4 Guest List
print('3-4')
guests = ['Ahmed', 'Rehan', 'Zeeshan']
invitations(guests)

# 3-5 Changing guest list
# lets say Ahmed is not comming to the party
print('3-5')
removedGuest = 'Ahmed'
guests.remove(removedGuest)
print('Sorry %s couldnt make it to the party\n\n' % removedGuest)
guests.insert(0,"Khan")#added new guest
invitations(guests)


# 3-6 Changing guest list
# Found a bigger table
print('3-6')
guests.insert(0,"Shahzad")#added new guest at the top
guests.insert(2,"Zain")#added new guest in the middle
guests.append("Ali")#added new guest at the end
invitations(guests)



# 3-6 Changing guest list
# Reducing the list
print('3-7')
#reduces list to 2
while len(guests)>2:
   guests.pop()

invitations(guests)

#removing the rest 2 invitees
del guests[1]
del guests[0]
#printed emptied list
print('Emptied List '+str(guests)+"\n\n\n\n")

#3-8
#unsorted raw list
destinations=["Paris","Karachi","Kathmandu","Seychelles","Maldives"]

print("Unsorted Destinations: " + str(destinations))#raw List
print("Sorted Destinations: "+str(sorted(destinations)))#Alphabatical Order
destinations.reverse()
print("Reversed: "+str(destinations))#unorderd reverse
destinations.reverse()
print("Reversed Again: "+str(destinations))#unorderd reverse again
destinations=sorted(destinations)
print("Reversed and Assigned: "+str(destinations))#unorderd reverse again
destinations=sorted(destinations.reverse())
print("Reverse Sorted: "+str(destinations))#unorderd reverse again