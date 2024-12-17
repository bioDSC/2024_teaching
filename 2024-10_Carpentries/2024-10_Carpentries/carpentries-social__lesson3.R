library(tidyverse)
library(here)

library(lubridate)


data_interviews <- read_csv(
  here("data", "SAFI_clean.csv"),  # note that this is equivalent to here("data/SAFI_clean.csv")
  na = "NULL")

    # file is at:
    # /Users/m.wehrens/Data_UVA/2024_teaching/2024-10_carpentries/data/SAFI_clean.csv

class(data_interviews)
class(data_interviews$key_ID)


######
# Some ways of looking at df through summary fns

# structure of the object and information about the class, length and content of each column
str(interviews) 

# summary statistics for each column
summary(interviews) 

# returns the number of columns and rows of the tibble, the names and class of each column, and previews as many values will fit on the screen. Unlike the other inspecting functions listed above, glimpse() is not a “base R” function so you need to have the dplyr or tibble packages loaded to be able to execute it.
glimpse(interviews) 

######
data_interviews[1] # note that tibble doesn't 'drop' like df does
data_interviews[,1]
as.data.frame(data_interviews)[,1] # drops

# -1 drops the first column, as opposed to python, where -1 is the last column
interviews[, -1] # 

# to re-order factor levels, simply use factor() with the levels argument
respondent_floor_type <- factor(c("earth", "cement", "cement", "earth"))
respondent_floor_type <- factor(respondent_floor_type, 
                                levels = c("earth", "cement"))

# to replace one level with another, use fct_recode()
respondent_floor_type <- fct_recode(respondent_floor_type, brick = "cement")

# can tell r that factor is ordered
respondent_floor_type <- factor(respondent_floor_type, 
                                levels = c("earth", "brick"), ordered = TRUE)

# a note about converting factors to numeric values
year_fct <- factor(c(1990, 1983, 1977, 1998, 1990))
as.numeric(year_fct)                     # Wrong! And there is no warning...
as.numeric(as.character(year_fct))       # Works...
as.numeric(levels(year_fct))[year_fct]   # The recommended way. (because internally, factors are stored as integers)

#####
# Plotting factors


## create a vector from the data frame column "memb_assoc"
memb_assoc <- interviews$memb_assoc
## convert it into a factor
memb_assoc <- as.factor(memb_assoc)
## let's see what it looks like
memb_assoc

# Bar plot
plot(memb_assoc)

# Now also show the NA values
memb_assoc <- interviews$memb_assoc
memb_assoc[is.na(memb_assoc)] <- "undetermined"
plot(factor(memb_assoc, levels=c('yes', 'no', 'undetermined')))

######
# Dates

# dates are stored as inconveninent strings
dates <- interviews$interview_date
dates

# Extract the separate parameters of the date
# This uses the lubridate package functions
interviews$day <- lubridate::day(dates)
interviews$month <- lubridate::month(dates)
interviews$year <- lubridate::year(dates)
interviews$year

# Conversely, lubridate can be used for formatting
char_dates <- c("7/31/2012", "8/9/2014", "4/30/2016")
lubridate::as_date(char_dates, format = "%m/%d/%Y", tz = "UTC") # note that without the tz argument, this didn't work ?!



