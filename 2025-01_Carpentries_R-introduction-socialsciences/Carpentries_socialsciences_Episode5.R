
################################################################################
# Episode 5: Data Wrangling with tidyr
# https://datacarpentry.github.io/r-socialsci/04-tidyr.html
################################################################################


# (A) X GO OVER STUFF (B) X ADD SOLUTIONS, (C) CHECK THE TEXT, 
    CONTINUE AT "PIVOTING WIDER" AND ELOBORATE THE SCRIPT BELOW
# (D) ADD WHAT IS LEARNED (E) CHECK SOLUTIONS

# TO DO (ADD WHAT WE'LL LEARN HERE)


# As before
library(tidyverse)
df_interviews <- readr::read_csv('data/SAFI_clean.csv', na="NULL")
    # View(df_interviews)

# Cheat sheet:
# https://raw.githubusercontent.com/rstudio/cheatsheets/main/tidyr.pdf



# keyID and instanceID supposedly unique values / interview
# Let's check that 

nrow(df_interviews)

df_interviews %>% 
  select(key_ID) %>% 
  distinct() %>% # keep only unique rows
  count()

# technical addition MW: could also be done like this:
# length(unique(df_interviews$key_ID))

df_interviews %>% 
  select(instanceID) %>% 
  distinct() %>% 
  count()

# This thus means the data is in the long format
# as each row = 1 observation

# It could be made longer, as the longest format would be
# id, observed variable, observed value
    # that's however unworkable

###

# look at part of the data
df_interviews %>%
  filter(village == "Chirodzo") %>%
  select(key_ID, village, interview_date, instanceID) %>%
  sample_n(size = 10)


###


# <SHOW SLIDE SHOW>

# Want to calculate summary about stuff people own ..
    # how??
    # Manipulate table, make it easy to count things

# View(interviews_items_owned)

# Build the following up per step, slowly..

interviews_items_owned <- df_interviews %>%
        separate_longer_delim(items_owned, delim = ";") %>%
            # the table becomes longer, expanded such that each row holds a value of the item
            ## View(interviews_items_owned)
        replace_na(list(items_owned = "no_listed_items")) %>%
            # NAs replaced
        mutate(items_owned_logical = TRUE) %>%
            # add TRUE param, this will be used in a moment 
            ## View(interviews_items_owned)
            ## <SHOW SLIDE>
        ## we also want to count the items
        # - can be done by separate table (group_by + summarize)
        # - but we want to add a column to "main table"
        group_by(key_ID) %>%
            # group again per observation
        # the following works, but *also counts no_listed_items*
        # mutate(number_items = n()) %>% 
        # so instead, we use "if_else"
        mutate(number_items = if_else(items_owned == "no_listed_items", 0, n())) %>% 
            # now count the items, note that mutate is also applied per group
            # what does "n" do?
            # ?n
            # --> counts group sizes
            ## View(interviews_items_owned)
        pivot_wider(names_from = items_owned,
                values_from = items_owned_logical,
                values_fill = list(items_owned_logical = FALSE))
            # keeps everything the same, except, importantly:
            # will take a column with categorical value;
            # make new columns of the values, filling it with values from a 2nd column
            # when information is missing, it will fill parameter X with a provided
            # default value
            # <SHOW SLIDE>

# Inspect final result
View(interviews_items_owned)
    # note that original items_owned column gone
    # dropped by pivot_wider()
    # duplicate it beforehand to avoid this

# now using this table, we can answer specific questions;

# E.g. number of people per village owning item X (bicycle) 
interviews_items_owned %>%
  filter(bicycle) %>%      # note bicycle is a boolean column now
  group_by(village) %>%
  count(bicycle)


# E.g. average number of owned items per village
interviews_items_owned %>%
    group_by(village) %>%
    summarize(mean_items = mean(number_items))

################################################################################

# EXERCISE
# 
# We created interviews_items_owned by reshaping the data: first longer and then wider. 
# Replicate this process with the months_lack_food column in the interviews dataframe. 
# Create a new dataframe with columns for each of the months filled with logical vectors 
# (TRUE or FALSE) and a summary column called number_months_lack_food that calculates the 
# number of months each household reported a lack of food.
# 
# Note that if the household did not lack food in the previous 12 months, 
# the value input was “none”.


# <GO OVER SOLUTION TOGETHER>






# solution

# my solution:
df_interviews_food <-
    df_interviews %>%
    # separate the months (and replace the NA values)
    separate_longer_delim(months_lack_food, delim = ';') %>% 
        # not used in official solution:
        # replace_na(list(months_lack_food='unknown')) %>% 
    # to facilitate counting
    group_by(key_ID) %>% 
    mutate(no_food = T, # add the true value to be used for alter pivot
           nr_months_no_food = if_else(months_lack_food == 'none', 0, n())) %>% # months without food
    # now pivot wider
    pivot_wider(names_from = months_lack_food, values_from = no_food, values_fill = F)
    

# Always check the result!    
View(df_interviews_food)


################################################################################





################################################################################
# Pivoting longer

# For some situations, also the inverse might be necessary
# This makes a table longer

interviews_long <- interviews_items_owned %>%
  pivot_longer(cols = bicycle:car,
               names_to = "items_owned",
               values_to = "items_owned_logical")

    # inverse, multiple columns -->
    # "collapse" into two single columns (name, and value)

    # let ppl try --> do they see?

View(interviews_items_owned)
View(interviews_long)

################################################################################
# EXERCISE

# We created some summary tables on interviews_items_owned using count and summarise.
# We can create the same tables on interviews_long, but this will require a 
# different process.
# 
# Make a table showing the number of respondents in each village who owned a particular 
# item, and include all items. The difference between this format and the wide format 
# is that you can now count all the items using the items_owned variable.



# <GO OVER SOLUTION TOGETHER>






# solution

# table with # respondents per village that own specific item
View(interviews_long)

interviews_long %>% 
    group_by(village, items_owned) %>% 
    filter(items_owned_logical == T) %>% 
    count()


################################################################################

## Clean data for plotting
interviews_plotting <- df_interviews %>%
  # as before, separate items owned, such that we get more rows
  separate_longer_delim(items_owned, delim = ";") %>%
  replace_na(list(items_owned = "no_listed_items")) %>%
  ## Again, add items logical, and also count the total items
  group_by(key_ID) %>% 
  mutate(items_owned_logical = TRUE,
         number_items = if_else(items_owned == "no_listed_items", 0, n())) %>% 
  # Now pivot wider again, like before
  pivot_wider(names_from = items_owned,
              values_from = items_owned_logical,
              values_fill = list(items_owned_logical = FALSE)) %>% 
  # Now do the same, but for months_lack_food
  separate_longer_delim(months_lack_food, delim = ";") %>%
  mutate(months_lack_food_logical = TRUE,
         number_months_lack_food = if_else(months_lack_food == "none", 0, n())) %>%
  pivot_wider(names_from = months_lack_food,
              values_from = months_lack_food_logical,
              values_fill = list(months_lack_food_logical = FALSE))

View(interviews_plotting)

################################################################################
# Exporting data

dir.create('data_output/')
readr::write_csv(interviews_plotting, file = "data_output/interviews_plotting.csv")


# can be loaded again also
interviews_plotting_loaded <- readr::read_csv('data_output/interviews_plotting.csv', na="NULL")
View(interviews_plotting_loaded)











