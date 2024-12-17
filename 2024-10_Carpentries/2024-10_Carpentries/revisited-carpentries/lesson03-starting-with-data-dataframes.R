

# Talking points file

# what is a data frame
    # motivate why it's used
    # tabular
    # columns are vectors

# SAFI data set
    # "Studying African Farmed-Led Irrigation)
    # study looking into farming an irrigation methods; data from interviews in Tanzania and Mozambique

# read_csv
    # readr package; included in tidyverse
    # conflicts
    # readr::read_csv
    # conflicted::conflict_scout()

# (skip the part about the "here" package)

# load file /Users/m.wehrens/Data_UVA/2024_teaching/2024-10_carpentries/data/SAFI_clean.csv
    # talk about file format, e.g. quotation marks and commas

    # class(data_interviews)
    # view, head
    # dim, nrow, ncol, head, tail, names, str, summary, glimpse

# subsetting dataframes
    # accessing elements, df[1,1], df[[1]], df[1:3, 7], df[3,], df[-1,], df[-c(7:131),], df['village'], df[,'village'], df['village']

# (..)






# quickly going over some solutions;
data_path_location = '/Users/m.wehrens/Data_UVA/2024_teaching/2024-10_carpentries/data/SAFI_clean.csv'
data_interviews = read_csv(data_path_location)



























