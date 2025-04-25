# Basic functions
str1 = "Jai"
str2 = "Shree"
str3 = "Shyam"

# Concatenation
str4 = str1 + " " + str2 + " " + str3
print(str4)

# Repetition
str5 = str1 * 3
print(str5)

# Slicing
str6 = str4[0:3]
print(str6)

# Length
str7 = len(str4)
print(str7)

# Membership
str8 = "Jai" in str4
print(str8)

# String methods
str9 = str4.lower()
print(str9)
str10 = str4.upper()
print(str10)
str11 = str4.title()
print(str11)
str12 = str4.replace("Jai", "Ram")
print(str12)

# String formatting
str13 = "Hello, {}. Welcome to {}.".format(str1, str2)
print(str13)
str14 = f"Hello, {str1}. Welcome to {str2}."
print(str14)

# String comparison
str15 = str1 == str2
print(str15)
str16 = str1 != str2
print(str16)

# String splitting
str17 = str4.split(" ")
print(str17)

# String joining
str18 = " ".join(str17)
print(str18)

# String stripping
str19 = "   Hello, World!   "
str20 = str19.strip()
print(str20)

# String counting
str21 = str4.count("Jai")
print(str21)

# String finding
str22 = str4.find("Shree")
print(str22)

# String replacing 
str23 = str4.replace("Shree", "Ram")
print(str23)