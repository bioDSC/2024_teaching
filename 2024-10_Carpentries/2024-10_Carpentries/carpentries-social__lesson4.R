
library(tidyverse)
# library(here)

path_data_analysis = '/Users/m.wehrens/Data_UVA/2024_teaching/2024-10_carpentries/'

data_interviews <- read_csv(
  paste0(path_data_analysis, 'data/SAFI_clean.csv'),
  na = "NULL")

# note that select is equivalent to subsetting using [,], 
# but with somewhat different options
select(data_interviews, village, no_membrs, months_lack_food)
select(data_interviews, village:respondent_wall_type)
select(data_interviews, 2:6)

colnames(data_interviews)

# similar, instead of using [,], the filter function can be used
filter(data_interviews, village == "Chirodzo",
                   rooms > 2,
                   no_meals > 2)

filter(data_interviews, village == "Chirodzo",rooms > 2|no_meals > 2)
filter(data_interviews, village %in% c("Chirodzo", "God"),rooms > 2|no_meals > 2)

######
# Pipes

# There are two Pipes in R: 
# 1) %>% (called magrittr pipe; made available via the 
# magrittr package, installed automatically with dplyr) 
# or 
# 2) |> (called native R pipe and it comes preinstalled 
# with R v4.1.0 onwards).

data_interviews_filsel <- 
    data_interviews %>%
        filter(village == "Chirodzo") %>%
        select(village:respondent_wall_type)

# exercise
# Using pipes, subset the interviews data to include interviews where respondents 
# were members of an irrigation association (memb_assoc) and retain only the 
# columns affect_conflicts, liv_count, and no_meals.

data_interviews_exercise <- 
    data_interviews %>% 
        filter(memb_assoc == 'yes') %>% 
        select(affect_conflicts, liv_count, no_meals)

# mutate function, this creates a new column in the data frame
data_interviews$people_per_room # doesn't exist yet
data_interviews_extended <-
    data_interviews %>%
        mutate(people_per_room = no_membrs / rooms)
data_interviews_extended$people_per_room # exists

# Exercise
# Create a new dataframe from the interviews data that meets 
# the following criteria: 
# contains only the village column and 
# a new column called total_meals containing a value that is
# equal to the total number of meals served in the household per
# day on average (no_membrs times no_meals). Only the rows where 
# total_meals is greater than 20 should be shown in the final dataframe.
data_interviews_exer2 <-
    data_interviews %>% 
        mutate(total_meals = no_membrs * no_meals) %>% 
        filter(total_meals > 20) %>% 
        select(village, total_meals)


#########
# Group by
# Allows you to perform summarizing functions on subsets of the data determined
# by a categorical parameter.
# This works together with the summarize function
# 
# ChatGPT: when you use the group_by() function in R (from the dplyr package),
# the grouping is stored as an attribute of the resulting dataframe. Specifically,
# the grouping information is stored in the "groups" attribute of the tibble
# (or dataframe) that group_by() returns.

# Specifically, the group function simply adds a lookup table which
# rows belong to which category.
data_interviews_grouped = group_by(data_interviews, village)
attributes(data_interviews_grouped)
attributes_data = attributes(data_interviews_grouped)
attributes_data$groups$.rows

# Now we can use the summarize function
data_interviews_summarized <-
    data_interviews %>%
        group_by(village) %>%
        summarize(mean_no_membrs = mean(no_membrs))
    # note that this return simply the group_by parameter
    # that was supplied, and the summary parameter that was 
    # defined

# Instead of summarize, you can also mutate
data_interviews_test <-
    data_interviews %>%
        group_by(village) %>%
        mutate(mean_no_membrs = mean(no_membrs))
View(data_interviews_test)

# Now presumably we can also do more complicated things:
colnames(data_interviews)
View(data_interviews)
# E.g. combinations of two categoricals
group_by(data_interviews, village, respondent_wall_type)
attributes(group_by(data_interviews, village, respondent_wall_type))$groups
# And also multiple summarize options
data_interviews_summarized2 <-
    data_interviews %>%
        group_by(village, respondent_wall_type) %>%
        summarize(mean_no_membrs = mean(no_membrs), median(years_liv))
data_interviews_summarized2
# grouping still exists
attributes(data_interviews_summarized2)$groups
data_interviews_summarized2_ng = ungroup(data_interviews_summarized2)
mean(data_interviews_summarized2$mean_no_membrs)
attributes(data_interviews_summarized2_ng)$groups # here, no grouping
    
# Ungrouping
# The output dataframe above is still grouped. 
# This can sometimes lead to undesirable behavior,
# and the grouping can be reset using the "ungroup" function
# which is also called above.

# arrange function changes order of rows by desired column
arrange(data_interviews, years_liv)
data_interviews %>%  arrange(years_liv)
# to produce descending order, use the (ugly?!) desc() function in between
data_interviews %>%  arrange(desc(years_liv))

# In my opinion, this is prettier, but OK
data_interviews[sort(data_interviews$years_liv,decreasing = T),]

# Count provides counts of a categorical variable
data_interviews %>%
    count(village)

























