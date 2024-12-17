
# Some code related to 
# https://datacarpentry.org/r-socialsci/

# For Justin's scrpits, see:
# https://github.com/justinchuntingho/Data_Carpentry

# Additional notes in MS Word:
# /Users/m.wehrens/Documents/TEACHING/Carpentries_2024-10/Notes R course carpentries-v2.docx

# Note they put both scripts and data in the same directory, 
# but I prefer to keep all my scripts together in a 
# git repository directory.
# So I've changed some code slightly.

getwd()

# Set up work directory
setwd('/Users/m.wehrens/Documents/git_repos/_UVA/2024teaching_notongityet/2024-10_Carpentries/2024-10_Carpentries/')
# setwd('/Users/m.wehrens/Data_UVA/2024_teaching/2024-10_carpentries/')
path_data_analysis = '/Users/m.wehrens/Data_UVA/2024_teaching/2024-10_carpentries/'

# create dirs
dir.create(paste0(path_data_analysis, "data"))
dir.create(paste0(path_data_analysis, "data_output"))
dir.create(paste0(path_data_analysis, "fig_output"))

# download file
download.file(
  "https://raw.githubusercontent.com/datacarpentry/r-socialsci/main/episodes/data/SAFI_clean.csv",
  paste0(path_data_analysis, "data/SAFI_clean.csv"), mode = "wb"
  )

######
# install packages
# check whether packages are in list of installed packages
# if not, install them
for (pkg in c("tidyverse", "here")) {
  if (!pkg %in% rownames(installed.packages())) {
    install.packages(pkg)
  }
    # install.packages('tidyverse')
    # install.packages('here')
}


#####
hh_members <- c(3, 7, 10, 6)
hh_members[hh_members >= 4 & hh_members <= 7]
hh_members[hh_members >= 4 | hh_members <= 7]

rooms <- c(2, 1, 1, NA, 7)
mean(rooms, na.rm = TRUE)
na.omit(rooms) # note that this automatically also returns additional attribute class (which is "omit")
rooms_nonna = na.omit(rooms)
rooms_nonna[c(1,2)] # but works normally

typeof(rooms) # gives type












