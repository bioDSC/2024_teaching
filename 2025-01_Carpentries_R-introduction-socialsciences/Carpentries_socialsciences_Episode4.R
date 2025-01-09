
################################################################################
# Episode 4: Data Wrangling with dplyr
# https://datacarpentry.github.io/r-socialsci/03-dplyr.html
################################################################################

# this episode is about working with tables and manipulating/selecting
# data from this table

# we'll use dplyr
# - 'data wrangling' easier (manipulation)
# - automatically loaded with the tidyverse

# about packages (= library)
# - contain function w/ pre written code
# - (not necessarily written in R, e.g. C++ also)
# - many packages are hosted at "Comprehensive R Archive Network" (CRAN)
# - install.packages()
# - library()
# - help(package='package_name')



## load the tidyverse
library(tidyverse)
# library(here) # SKIPPED



df_interviews <- readr::read_csv('data/SAFI_clean.csv', na="NULL")

## inspect the data
df_interviews

## preview the data
# view(interviews)


####

# to select columns throughout the dataframe
select(df_interviews, village, no_membrs, months_lack_food)
# to do the same thing with subsetting
df_interviews[c("village","no_membrs","months_lack_food")]
# to select a series of connected columns
select(df_interviews, village:respondent_wall_type)

    # so select is a bit of an "atypical" function,
    # since it can accept values without quotation marks
    # 
    # select will be convenient later, when applying multiple 
    # operations to your data frame

####


# filters observations where village name is "Chirodzo"
filter(df_interviews, village == "Chirodzo")



####

# filters observations with "and" operator (comma)
# output dataframe satisfies ALL specified conditions
filter(df_interviews, village == "Chirodzo",
                   rooms > 1,
                   no_meals > 2)

# this is equal to:
filter(interviews, village == "Chirodzo" &
                   rooms > 1 &
                   no_meals > 2)

# Addition MW:
TRUE & TRUE
TRUE & FALSE
FALSE & TRUE
FALSE & FALSE

# filters observations with "|" logical operator ["or"]
# output dataframe satisfies AT LEAST ONE of the specified conditions
filter(interviews, village == "Chirodzo" | village == "Ruaca")

# Addition MW:
TRUE | TRUE
TRUE | FALSE
FALSE | TRUE
FALSE | FALSE



##### Combining operations


# Approach 1: using intermediate steps
# filter
df_interviews2 <- filter(df_interviews, village == "Chirodzo")
# select specific cols
df_interviews_ch <- select(df_interviews2, village:respondent_wall_type)

# Approach 2: nested functions
# This can also be done in one line, by directly putting some code
# as input argument to a function
df_interviews_ch <- select(filter(df_interviews, village == "Chirodzo"),
                         village:respondent_wall_type)
    # with multiple steps, this will become chaotic

# Approach 3: pipe operator
# The pipe operator (%>%) can be used to achieve the same
# Quickly type it: CTRL+SHIFT+M(windows)/CMD+SHIFT+M(mac)
# It will "forward" the output of a function to the first argument
# of another function
    # There's a built-in pipe (|>)
    # There's the %>% pipe, which cmomes with the tidyverse/magrittr package
        # the %>% is a bit more flexible, but requires the package

# the following example is run using magrittr pipe but the output will be same with the native pipe
df_interviews %>%
    filter(village == "Chirodzo") %>%
    select(village:respondent_wall_type)


# Do the same, but put the result in an output parameter
df_interviews_ch <- df_interviews %>%
    filter(village == "Chirodzo") %>%
    select(village:respondent_wall_type)

df_interviews_ch

################################################################################
# EXERCISE


# Using pipes, subset the interviews data to include interviews where
# respondents were members of an irrigation association (memb_assoc) 
# and retain only the columns affect_conflicts, liv_count, and no_meals.



# < LOOK AT SOLUTION TOGETHER>





# SOLUTION
df_interviews %>%
    filter(memb_assoc == 'yes') %>%
    select(affect_conflicts, liv_count, no_meals)


################################################################################
# Mutate

# You often want to manipulate values in your dataframe
# (For example, normalization of cell counts)
# mutate() creates new columns that are functions of existing variables.

df_interviews %>%
    mutate(people_per_room = no_membrs / rooms)

# perhaps we're interested in seeing whether members of being
# a member  of a farming association is related to the amount of
# meals each day

# Can also be combined with other operations
df_interviews %>%
    filter(!is.na(memb_assoc)) %>% # filter non-NA answers
    mutate(people_per_room = no_membrs / rooms) # ppl/room

    # note that the "!" reverses a logical value 
    # 'negation operator'

################################################################################

# Exercise
# Create a new dataframe from the interviews data that meets the following criteria:
# contains only the village column and a new column called total_meals containing a 
# value that is equal to the total number of meals served in the household per day 
# on average (no_membrs times no_meals). Only the rows where total_meals is greater 
# than 20 should be shown in the final dataframe.
# 
# Hint: think about how the commands should be ordered to produce this data frame!


# <GO THROUGH SOLUTION TOGETHER>




# Solution

# What do we want?
#
# only village column
# total_meals = no_membrs*no_meals
# only rows with total_meals > 20

df_interviews %>%
    # create new col
    mutate(total_meals = no_membrs*no_meals) %>%
    # select total_meals > 20
    filter(total_meals > 20) %>%
    # select desired columns
    select(village, total_meals)



################################################################################



################################################################################
# Split-apply-combine data analysis and the summarize() function


# Often, you might want to analyze a subset of your data (e.g. cells or conditions)
# 
# The group_by function can be used to let R know which groups you are interested in
# The summary function can then calculate summary parameters for those groups
# ("collapses data")


df_interviews %>%
    group_by(village) %>%
    summarize(mean_no_membrs = mean(no_membrs))

    # Technical note to self:
    # groups are stored as an attribute of the dataframe,
    # can be accessed by:
    # df_interviews_grouped <- group_by(df_interviews, village)
    # attributes(df_interviews_grouped)$groups 

# Grouping can also be done for combinations of parameters
df_interviews %>%
    group_by(village, memb_assoc) %>%
    summarize(mean_no_membrs = mean(no_membrs))


# in this case, the output of summarize will retain some of the grouping
# see the second line of the output above "# A tibble: 9 × 3 // # Groups:   village [3]"

# "ungroup" removes any (left-over) grouping
# (avoid unexpected behavior later)
df_interviews %>%
    group_by(village, memb_assoc) %>%
    summarize(mean_no_membrs = mean(no_membrs)) %>%
    ungroup()

# Can be combined further
df_interviews %>%
    filter(!is.na(memb_assoc)) %>% # added filter to remove NAs in memb_assoc
    group_by(village, memb_assoc) %>%
    summarize(mean_no_membrs = mean(no_membrs))


# Multiple summary statisics can be calculated
df_interviews %>%
    filter(!is.na(memb_assoc)) %>%
    group_by(village, memb_assoc) %>%
    summarize(mean_no_membrs = mean(no_membrs),
              min_membrs = min(no_membrs)) # addition of min(no_membrs)

# and the df can also be sorted as desired
df_interviews %>%
    filter(!is.na(memb_assoc)) %>%
    group_by(village, memb_assoc) %>%
    summarize(mean_no_membrs = mean(no_membrs),
              min_membrs = min(no_membrs)) %>%
    arrange(min_membrs) 

    

# To invert order, use desc, or "-min_membrs"
df_interviews %>%
    filter(!is.na(memb_assoc)) %>%
    group_by(village, memb_assoc) %>%
    summarize(mean_no_membrs = mean(no_membrs),
              min_membrs = min(no_membrs)) %>%
    arrange(desc(min_membrs))

# note to self: desc effectively produces "-min_membrs" but is generalized, e.g. 
# desc(factor(letters))


# "Count" can count instances of a certain group
df_interviews %>%
    count(village)
df_interviews %>%
    count(village, sort = TRUE)


################################################################################
# EXERCISES


# (A)
# How many households in the survey have an average of two meals per day? 
# Three meals per day? Are there any other numbers of meals represented?
#
# (B)
# Use group_by() and summarize() to find the mean, min, and max number 
# of household members for each village. 
# Also add the number of observations (hint: see ?n).    
# (C)
# What was the largest household interviewed in each month?


# <GO OVER SOLUTIONS TOGETHER>





# Solutions

# (A)
View(df_interviews)
df_interviews %>%
    count(no_meals)

# (B)
df_interviews %>%
    group_by(village) %>%
    summarize(mean_membrs = mean(no_membrs), 
              min_membrs = min(no_membrs), 
              max_membrs = max(no_membrs))

# (C) 
df_interviews %>%
    # First add years and months
    mutate(
        # PAY ATTENTION HERE! MONTHS ARE POTENTIALLY NOT UNIQUE
        year = year(df_interviews$interview_date), 
        month = month(df_interviews$interview_date)) %>%
    group_by(year, month) %>%
    summarize(mean_membrs = mean(no_membrs), # optional
              min_membrs = min(no_membrs), # optional
              max_membrs = max(no_membrs))


################################################################################

# Key Points
#
# Use the dplyr package to manipulate dataframes.
# Use select() to choose variables from a dataframe.
# Use filter() to choose data based on values.
# Use group_by() and summarize() to work with subsets of data.
# Use mutate() to create new variables.









