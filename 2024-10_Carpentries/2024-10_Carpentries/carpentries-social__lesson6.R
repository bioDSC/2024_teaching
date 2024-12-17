library(tidyverse)
library(here)
library(ggplot2)



path_data_analysis = '/Users/m.wehrens/Data_UVA/2024_teaching/2024-10_carpentries/'

# download data
download.file(
  "https://raw.githubusercontent.com/datacarpentry/r-socialsci/main/episodes/data/interviews_plotting.csv",
  paste0(path_data_analysis, "data/interviews_plotting.csv"), mode = "wb"
  )

# load data
dataset_interviews_plotting <- read_csv(
  paste0(path_data_analysis, "data/interviews_plotting.csv"),
  na = "NULL")

# this can also be done directly
# dataset_interviews_plotting <- read_csv("https://raw.githubusercontent.com/datacarpentry/r-socialsci/main/episodes/data/interviews_plotting.csv")
#
# See also the alternative tab for some advanced data wrangling

# Example plot
# This provides a scatter
# Interestingly, since the data are integers, we can
# also use the jitter plot here to split up those
# "categorical" data
# (I was used to a specific use case for the jitter
# plot only, which uses it on categorical data)
dataset_interviews_plotting %>%
    ggplot(aes(x = no_membrs, y = number_items)) +
    geom_point()

# 
dataset_interviews_plotting %>%
    ggplot(aes(x = no_membrs, y = number_items)) +
    geom_jitter(alpha = 0.3,
                width = 0.2,  # amount of random motion, defaults to 40% of the resolution of the data 
                height = 0.2)

# a nice alternative way to plot overlaying data points is 
# the following, in which geom_count adds the occurances
dataset_interviews_plotting %>%
   ggplot(aes(x = no_membrs, y = number_items, color = village)) +
   geom_count() # this also appears to correctly order the colors such that all categories are visible

# Exercise:
# Use what you just learned to create a scatter plot of rooms by village with the 
# respondent_wall_type showing in different colours. Does this seem like a good 
# way to display the relationship between these variables? What other kinds of 
# plots might you use to show this type of data?
# What they provided:
dataset_interviews_plotting %>%
   ggplot(aes(x = rooms, y = village, color = respondent_wall_type)) +
   geom_count()
# better way:
dataset_interviews_plotting %>%
    ggplot(aes(x = respondent_wall_type , y = rooms, color = village)) +
    # now add a jitter which separates the colored points by using dodge
    geom_count(position = position_dodge(width = 0.5))+theme_bw()

# they actually also go on to suggest that geom_jitter is a better option
plt.base <- dataset_interviews_plotting %>%
    ggplot(aes(x = respondent_wall_type , y = rooms, color = village)) +
    theme_bw()

# now add a jitter which separates the colored points by using dodge
plt.base + geom_violin(position = position_dodge(width = 0.5))

# could also use a kde estimte of density
fct_walltype=as.factor(dataset_interviews_plotting$respondent_wall_type)
ggplot(dataset_interviews_plotting, aes(x= as.numeric(as.factor(respondent_wall_type)), y=rooms, color=village)) + 
    geom_density_2d(bins=3)+
    ylim(0,5)+theme_bw()+
    # now add labels of respondent_wall_type back, but keep xlim at 0,5
    scale_x_continuous(breaks = 1:max(as.numeric(fct_walltype)), labels = levels(fct_walltype), limits = c(0,5))
    
# add a boxplot overlay that's narrow, with see-through face and black outline
plt.base + geom_boxplot(position = position_dodge(width = 0.5), width=.2)
        # fill=NA will make it see through but destory the ordering
# alternative to using dodge
plt.base + geom_boxplot(position = "dodge", width=.2)

# Usig tile, after summarizig the data that we're interested inn
# Not really convenient, because it hides a load of the data
dataset_interviews_plotting %>%
    group_by(village, respondent_wall_type) %>%
    summarize(mean_rooms = mean(rooms)) %>%
    ggplot(aes(x = village, y = respondent_wall_type, fill = mean_rooms)) +
    geom_tile()+
    # define a custom gradient to set the scale for geom_tile
    scale_fill_gradient(low = "white", high = "red")
    
    
dataset_interviews_plotting %>%
    ggplot(aes(x = respondent_wall_type)) +
    geom_bar(aes(fill = village))+theme_bw()


dataset_interviews_plotting %>%
    ggplot(aes(x = respondent_wall_type)) +
    geom_bar()+theme_bw()

# now do the same, but order x-axis by count
dataset_interviews_plotting %>%
    ggplot(aes(x = respondent_wall_type)) +
    geom_bar()+theme_bw()+
    scale_x_discrete(limits = names(sort(table(dataset_interviews_plotting$respondent_wall_type), 
                                         decreasing = TRUE)))


###

# alternative to use dodge
dataset_interviews_plotting %>%
    ggplot(aes(x = respondent_wall_type)) +
    geom_bar(aes(fill = village), position = "dodge")+theme_bw()


####

# What if we wanted to see the proportion of respondents in each village
# who owned a particular item? We can calculate the percent of people
# in each village who own each item and then create a faceted series of
# bar plots where each plot is a particular item. First we need to
# calculate the percentage of people in each village who own each item:

# Below, some additional functions are used
# (Code from Justin, the carpentries uses even more complicated code)

# gather converts the data from wide to long format

# the code below, step by step, does the following:
# 1. gather the columns from bicycle to no_listed_items into a single column
#    the items_owned_logical column will contain the values of the columns
# 2. filter the data to only include rows where items_owned_logical is TRUE
# 3. count the number of people in each village who own each item
# 4. add a column with the number of people in each village
#    this could be done alternatively by using a lookup table
# 5. calculate the percentage of people in each village who own each item

# Code justin (with some added comments)
percent_items <- interviews_plotting %>%
    gather(items, items_owned_logical, bicycle:no_listed_items) %>%
    filter(items_owned_logical) %>% # here simply removes items which are FALSE
    count(items, village) %>%
    ## add a column with the number of people in each village
    mutate(people_in_village = case_when(village == "Chirodzo" ~ 39,
                                         village == "God" ~ 43,
                                         village == "Ruaca" ~ 49)) %>%
    mutate(percent = n / people_in_village)

# using a lookup table
# village size
village_size <-
    interviews_plotting %>% 
        group_by(village) %>%
        summarize(n = n())
village_size_lookup = vilage_size$n
names(village_size_lookup) = vilage_size$village

percent_items_MW <- interviews_plotting %>%
    gather(items, items_owned_logical, bicycle:no_listed_items) %>%
    filter(items_owned_logical) %>% # here simply removes items which are FALSE
    count(items, village) %>%
    ## add a column with the number of people in each village
    mutate(people_in_village = village_size_lookup[village]) %>%
    mutate(percent = n / people_in_village)


View(percent_items)
View(percent_items_MW)
