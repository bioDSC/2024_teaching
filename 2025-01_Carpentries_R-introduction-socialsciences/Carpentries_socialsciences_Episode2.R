
################################################################################
# Episode 2: "Introduction to R"
# https://datacarpentry.github.io/r-socialsci/01-intro-to-r.html
################################################################################
# Print this for myself, type things as I go over it


# typing math
3 + 5
12/7

# objects
    # everything is an object
    # <- operator
area_hectares <- 1.0

# naming of objects
    # cannot start with number
    # case sensitive
    # names that are already in use
    # avoid some names, e.g. "mean", "T", avoid dots

# using (x<-1) to print value
(area_hectares <- 1.0)

2.47 * area_hectares
area_hectares <- 2.5
2.47 * area_hectares

area_acres <- 2.47 * area_hectares

area_hectares <- 50

########################################
# EXERCISE
# What is the value of area_acres currently?
########################################

# Comments
# For others, for future self
# Key to reproducible analysis
# (mac) CMD+SHIFT+C / (windows) CTRL+SHIFT+C


# (OPEN POWERPOINT AGAIN HERE, SLIDE PROJECT MANAGMENT)


########################################
# Exercise
# 
# Create two variables r_length and r_width and assign them values. It should be noted that, 
# because length is a built-in R function, R Studio might add “()” after you type length and 
# if you leave the parentheses you will get unexpected results. This is why you might see 
# other programmers abbreviate common words. Create a third variable r_area and give it a value 
# based on the current values of r_length and r_width. Show that changing the values of either 
# r_length and r_width does not affect the value of r_area.



# <GO OVER SOLUTION TOGETHER>


########################################

# Functions and arguments
    # "Canned scripts"
    # (can be packaged in libraries)
    # e.g. function "sqrt()"
    # functions can be "called" and have "arguments" (input), and "return value" (output)

b <- sqrt(a)
    # value of a is given as input
    # function calculates and returns something new
    # anything can be returned
    # here, one value, sqrt, is returned
    
round(3.14159)

# help function

round(3.14159, digits=2)
round(3.14159, 2)
round(digits=2, x=3.14159)


########################################
# Exercise
# 
# Type in ?round at the console and then look at the output in the Help pane. 
# What other functions exist that are similar to round? How do you use the digits 
# parameter in the round function?


# <GO OVER SOLUTION TOGETHER>



########################################


################################################################################
# Vectors and data types

# A vector is a series of values
# numbers, characters

# number of members of households
hh_members <- c(3, 7, 10, 5)
hh_members

# and wall types in their houses
resp_wall_type <- c('muddaub', 'burntbricks', 'sunbricks')
resp_wall_type

# note there are quotes!

length(hh_members)
length(resp_wall_type)

typeof(hh_members) 
typeof(resp_wall_type)

# str() provides overview of the structure of object and its elements
str(hh_members) 
    # (!= python str)
    # e.g.
    as.character(hh_members)

#####
    
# c() can be used to add things to a vector
possessions <- c('bycicle', 'radio', 'television')
possessions <- c(possessions, 'mobile_phone') # add at start
posesesions <- c('car', possessions) # add at beginning

# atomic vector
    # vector of single type
        # character
        # numeric/double
        # logical
        # integer
        # (complex)
        # (raw)

################################################################################
# EXERCISE
# 
# (A)
# We’ve seen that atomic vectors can be of type character, numeric (or double), 
# integer, and logical. But what happens if we try to mix these types in a single vector?
# 
# (B)
# What will happen in each of these examples? (hint: use class() to check the data type of your objects):
# 
# R
# num_char <- c(1, 2, 3, "a")
# num_logical <- c(1, 2, 3, TRUE)
# char_logical <- c("a", "b", "c", TRUE)
# tricky <- c(1, 2, 3, "4")
# Why do you think it happens?
# 
# (C)
# How many values in combined_logical are "TRUE" (as a character) in the following example:
# 
# R
# num_logical <- c(1, 2, 3, TRUE)
# char_logical <- c("a", "b", "c", TRUE)
# combined_logical <- c(num_logical, char_logical)
#
# (D)
# You’ve probably noticed that objects of different types get converted into a single, 
# shared type within a vector. In R, we call converting objects from one class into
# another class coercion. These conversions happen according to a hierarchy, whereby 
# some types get preferentially coerced into other types. Can you draw a diagram that
# represents the hierarchy of how these data types are coerced?



# <GO OVER SOLUTION TOGETHER>



# Solution:
typeof(c(1.0, integer(1), 'a', T))
typeof(c(1.0, integer(1), T))
typeof(c(integer(1), T))
typeof(c(T))



################################################################################
# Subsetting vectors

respondent_wall_type <- c("muddaub", "burntbricks", "sunbricks")
respondent_wall_type[2]

respondent_wall_type[c(3, 2)]

more_respondent_wall_type <- respondent_wall_type[c(1, 2, 3, 2, 1, 3)]
more_respondent_wall_type

# conditional subsettings
hh_members <- c(3, 7, 10, 6)
hh_members[c(TRUE, FALSE, TRUE, TRUE)]

hh_members > 5

hh_members[hh_members > 5]

# using AND and OR
hh_members[hh_members < 4 | hh_members > 7]
hh_members[hh_members >= 4 & hh_members <= 7]

    # explain greater than and less than
    # == means equal to

# Continued, new example
possessions <- c("car", "bicycle", "radio", "television", "mobile_phone")
possessions[possessions == "car" | possessions == "bicycle"] # returns both car and bicycle


# %in%
possessions %in% c("car", "bicycle")
possessions %in% c("car", "bicycle", "motorcycle", "truck", "boat", "bus") 
    # e.g. bus is not in possessions, still works

possessions[possessions %in% c("car", "bicycle", "motorcycle", "truck", "boat", "bus")]


################################################################################
# Missing data

# R designed for data
    # includes concept of "missing data"
    # many functions include option to handle missing data

# amount of rooms in house of respondents
rooms <- c(2, 1, 1, NA, 7)
mean(rooms)

max(rooms)



mean(rooms, na.rm = TRUE)
max(rooms, na.rm = TRUE)


# convenient additional functions
is.na(rooms)
na.omit(rooms)
complete.cases(rooms)


# The "not" operator
rooms[!is.na(rooms)]

sum(is.na(rooms))

rooms[complete.cases(rooms)]

################################################################################
# Exercise
#
# 1. Using this vector of rooms, create a new vector with the NAs removed.
# rooms <- c(1, 2, 1, 1, NA, 3, 1, 3, 2, 1, 1, 8, 3, 1, NA, 1)
# 
# 2. Use the function median() to calculate the median of the rooms vector.
# 
# 3. Use R to figure out how many households in the set use more than 2 rooms for sleeping.



# <GO OVER SOLUTION TOGETHER>



################################################################################


# (end of episode)

# We are ready for the SAFI dataset!


# SAFI (Studying African Farmer-Led Irrigation) is a study looking at farming 
# and irrigation methods in Tanzania and Mozambique. The survey data was collected 
# through interviews conducted between November 2016 and June 2017.





























































