lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim" , "Yogi" , "Toby"]
friends.extend(lucky_numbers) #adding two strings together
friends.append("Creed") #adding new element
friends.insert(1, "kelly") #adding new element by putting its index number
friends.remove("Jim") #removing jim
#friends.sort() #arranging in ascending order
print(friends)
print(friends.index("Kevin")) #how to find the element in the lists
