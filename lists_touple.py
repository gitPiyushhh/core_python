random = ["John", "Doe", 20, "Computer Science"]

# Can be changed
print(random[0])

random[0] = "Jane"
print(random[0])

# Slicing
print(random[0:2])

# Appending
random.append("Mathematics")
print(random)

# Pop
random.pop()
print(random) # Pop last element(default) else also can have the indez

#######################################
### Tuple

random_tuple = ("John", "Doe", 20, "Computer Science")

# Can not be changed
print(random_tuple[0]) 
print(random_tuple[0:2])
# random_tuple[0] = "Jane" # This will give an error
# random_tuple.append("Mathematics") # This will give an error
# random_tuple.pop() # This will give an error
# random_tuple.pop(0) # This will give an error


#######################################
### Pratice Problems
# 1. Create a list of fav movies

movies = []
mov = input("Enter your fav movie: ")
movies.append(mov)
mov = input("Enter your fav movie: ")
movies.append(mov)
mov = input("Enter your fav movie: ")
movies.append(mov)

print(movies)

# 2. Check palindrome
lst = [1, 2, 3, 2, 1]

for i in range(len(lst)//2):
    if lst[i] != lst[len(lst)-i-1]:
        print("Not a palindrome")
        break
else:
    print("Palindrome")