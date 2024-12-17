
################################################################################
# Lesson 3: "Starting with data"
################################################################################
# Print this for myself, type things as I go over it


# what is a data frame
    # motivate why it's used
    # tabular
    # columns are vectors

# (off script)
# Can be made by hand
df_cats =
    data.frame(name=c('Mittens', 'General', 'Hans'),
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
    # 
    # accessing elements, df[1,1], df[[1]], df[1:3, 7], df[3,], 
    # df[-1,], df[-c(7:131),], df['village'], df[,'village'], df['village']

# ("tip") perhaps unexpected normal dataframe behavior
df_interviews[,1]  # Tibble remains tibble
df_interviews2[,1] # 'normal' dataframe 'drops' identity and simplifies
df_interviews2[,1, drop=FALSE]


!!!!!!! CONTINUE HERE !!!!!!!
continue at ep.3, 'subsetting dataframes'
!!!!!!! CONTINUE HERE !!!!!!!





















