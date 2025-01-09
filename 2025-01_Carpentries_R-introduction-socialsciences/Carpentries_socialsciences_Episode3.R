
################################################################################
# Episode 3: "Starting with data"
# https://datacarpentry.github.io/r-socialsci/02-starting-with-data.html
################################################################################
# Print this for myself, type things as I go over it


# what is a data frame
    # motivate why it's used
    # tabular
    # columns are vectors

# (off script)
# Can be made by hand
df_cats =
    data.frame(cat_name=c('Mittens', 'General', 'Hans'),
               age=c(1, 4, 5), potty_trained=c(T, T, F))
View(df_cats)

# SAFI data set
    # "Studying African Farmed-Led Irrigation)
    # study looking into farming an irrigation methods; data from interviews in Tanzania and Mozambique


# read_csv
    # readr package; included in tidyverse
    # conflicts 
    # readr::read_csv
        # talk about file format, e.g. quotation marks and commas
        # read_table(), read_tsv(), several options
            # Google & help function are your friend!
    # conflicted::conflict_scout()

# (skip the part about the "here" package)

# load file /Users/m.wehrens/Data_UVA/2024_teaching/2024-10_carpentries/data/SAFI_clean.csv
    # For description of data, see powerpoint, or
    # https://datacarpentry.github.io/r-socialsci/instructor/02-starting-with-data.html

    # class(data_interviews)

library(tidyverse)
df_interviews <- readr::read_csv('data/SAFI_clean.csv', na="NULL")
View(df_interviews)

# Same result:
data_path_location = '/Users/m.wehrens/Data_UVA/2024_teaching/2024-10_carpentries/data/SAFI_clean.csv'
df_interviews = readr::read_csv(data_path_location, na="NULL")
    # About the "na" parameter
    # Character vector of strings to interpret as missing values. 
    # Set this option to character() to indicate no missing values.
View(df_interviews)

# Tibble
    # data frame is loaded as a "tibble" here,
    # bit of technical background, is an extension
    # of the 'normal' data.frame
    # 
    # object of class "tibble"; you can see class by:
    class(df_interviews)

# read.csv similar function, but slightly different behavior
# NOTE: difference in function name is the dot/underscore
df_interviews2 = read.csv(data_path_location, na="NULL")    
    # e.g. spaces in colnames handled differently
    # importantly: results in 'normal' data.frame object


# when printing in console
df_interviews
    # now we can see (abbreviated) which type of data the column is


# Functions that give you important dataframe properties:
    # View, head
    # dim, nrow, ncol, head, tail, names, str, summary, glimpse

# we might be interest in only a part of the data:
# (e.g. in an RNA-seq experiment, only cells of a certain type,
# or here, investigate answers that have a specific feature)
# subsetting dataframes
    # 
    # coordinates: df[row, col]

# accessing elements

df_interviews[1,1]
df_interviews[1:3, 7]
df_interviews[3,]
df_interviews[-1,]
df_interviews[-c(7:131),]
df_interviews['village']
df_interviews[,'village']
df_interviews[[1]] # produces vector!
df_interviews[['village']] # produces vector!
df_interviews$village # produces vector!

# ("tip") perhaps unexpected normal dataframe behavior
df_interviews[,1]  # Tibble remains tibble
df_interviews2[,1] # 'normal' dataframe 'drops' identity and simplifies
df_interviews2[,1, drop=FALSE]

################################################################################
# EXERCISE

# (A)
# Create a tibble (interviews_100) containing only the data in row 100 of the interviews dataset.
#
# Now, continue using interviews for each of the following activities:
# (B)
# Notice how nrow() gave you the number of rows in the tibble?
# Use that number to pull out just that last row in the tibble.
# (C) 
# Compare that with what you see as the last row using tail() to make sure it’s meeting expectations.
# (D)
# Pull out that last row using nrow() instead of the row number.
# (E)
# Create a new tibble (interviews_last) from that last row.
# (F)
# Using the number of rows in the interviews dataset that you found earlier, 
# extract the row that is in the middle of the dataset. 
# Store the content of this middle row in an object named interviews_middle. 
# (hint: This dataset has an odd number of rows, so finding the middle is 
# a bit trickier than dividing n_rows by 2. Use the median( ) function and 
# what you’ve learned about sequences in R to extract the middle row!)
# 
# (G)
# Combine nrow() with the "-" (ie minus) notation above to reproduce the behavior of 
# head(interviews), keeping just the first through 6th rows of the interviews dataset.


# <GO OVER SOLUTION TOGETHER>


################################################################################



################################################################################
# Factors
# To store categorical variables, e.g. categories or groups with a fixed number of values

respondent_floor_type <- factor(c("earth", "cement", "cement", "earth"))
levels(respondent_floor_type)
nlevels(respondent_floor_type)

    # note that "under the hood", these are stored as integers
    # could use integers, but less descriptive

    # be careful with conversions

# factors can be re-ordered
respondent_floor_type # current order

### re-order
respondent_floor_type <- factor(respondent_floor_type, 
                                levels = c("earth", "cement"))

respondent_floor_type # after re-ordering


### altering values of levels
# before
respondent_floor_type 
levels(respondent_floor_type)

# change
respondent_floor_type <- fct_recode(respondent_floor_type, 
                                    brick = "cement") # cement to brick

# after
respondent_floor_type 
levels(respondent_floor_type)

## technical alternative
# levels(respondent_floor_type)[2] <- "brick"

### Nominal and ordinal variables
# Nominal = unordered categories
# Ordinal = ordered categories (non-equal intervals)

respondent_floor_type_ordered <- factor(respondent_floor_type, 
                                        ordered = TRUE)

respondent_floor_type_ordered # after setting as ordered factor

### Converting factors

as.character(respondent_floor_type)

# converting numbers is tricky
year_fct <- factor(c(1990, 1983, 1977, 1998, 1990))
as.numeric(year_fct) # Wrong! And there is no warning...

# note that the values here are strings, but quotes are not shown
year_fct 
respondent_floor_type # see also respondent_floor_type

# How to convert:
as.numeric(as.character(year_fct))       # Works...
    # perhaps break this down quickly

as.numeric(levels(year_fct))[year_fct]   # The recommended way.

# break this down:
levels_year_fct <- levels(year_fct) 
levels_year_fct # array with strings
levels_year_fct_num <- as.numeric(levels_year_fct) # convert those to numeric values
levels_year_fct_num # list of the categories, as numeric 
levels_year_fct_num[year_fct] # now use indexing (year_fct can be used as integer!) 
                              # to recover the original sequence of elements

### Renaming factors

# We can inspect the distribution of whether interview respondents 
# where member of a farming association

memb_assoc <- df_interviews$memb_assoc
memb_assoc <- as.factor(memb_assoc)

# inspect
memb_assoc
# plot
plot(memb_assoc) # doesn't show the NAs however!


# Let's address this
memb_assoc <- df_interviews$memb_assoc
memb_assoc[is.na(memb_assoc)] <- "undetermined"
memb_assoc <- as.factor(memb_assoc)
memb_assoc
plot(memb_assoc)


################################################################################
# Exercise

# (A)
# Rename the levels of the factor to have the first letter in uppercase: “No”,“Undetermined”, and “Yes”.
# 
# (B)
# Now that we have renamed the factor level to “Undetermined”, can you 
# recreate the barplot such that “Undetermined” is last (after “Yes”)?



# <GO OVER SOLUTION TOGETHER>






# solution:
# use fct_recode and change order of levels
memb_assoc <- fct_recode(memb_assoc, No="no", Yes="yes", Undetermined="undetermined")
memb_assoc <- factor( memb_assoc, levels=c("No", "Yes", "Undetermined"))
plot(memb_assoc)

################################################################################

################################################################################
# Handling dates

# LET'S GO OVER THIS QUICKLY

library(lubridate) # standard included

# Most convenient format to store dates is:
# YYYY-MM-DD (or YYYYMMDD) as it can be easily sorted chronologically ("alphabetically")

dates <- df_interviews$interview_date
str(dates) # inspect --> this is already in the correct form

# convenient to add separately
df_interviews$day <- day(dates)
df_interviews$month <- month(dates)
df_interviews$year <- year(dates)
View(df_interviews)

# What if we have an incovenient format?
char_dates <- c("7/31/2012", "8/9/2014", "4/30/2016")
str(char_dates)

as_date(char_dates, format = "%m/%d/%Y")
    # note that as_date is from the lubridate package, see:
    # ?as_date

# The formatting must be precise
as_date(char_dates, format = "%m/%d/%y") # will fail

# SKIP:
ymd("2022-12-15")
mdy(char_dates)
dmy("15-01-12")







