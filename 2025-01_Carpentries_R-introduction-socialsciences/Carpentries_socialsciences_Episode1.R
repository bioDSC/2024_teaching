
################################################################################
# Episode 1: "Before we Start"
# https://datacarpentry.github.io/r-socialsci/00-intro.html

# Repository:
# https://github.com/bioDSC/2024_teaching/tree/main/2025-01_Carpentries_R-introduction-socialsciences
################################################################################

# R vs. Rstudio
    # R: language + interpretation software
    # RStudio: software that makes interaction w/ R easier

# Why R
    # Excel/graphpad: Clicking; irreproducible
    # R: Point by point recipe
        # easier to repeat / fix mistakes
        # managing complex tasks
        # much pre-written code exists ("libraries"/"packages")
        # free, open source, cross-platform

# Setting up

# Getting started
    # File >> New project (show in new window)
        # Work on several projects
        # Keep things together that belong together
    # (Switch to slideshow show folder structures)

# About RStudio
    # (not R!)
    # File editor ("source")
    # Console, R without the editor
    # Environment (top right)
    # Files, plots, help (bottom right)

# First lines of code
    # comments (#)
    # using my first functions
    # use getwd, setwd
    # use dir.create to create a data directory
    # download a file to that directory, "download.file"
    # the file: "https://raw.githubusercontent.com/datacarpentry/r-socialsci/main/episodes/data/SAFI_clean.csv"

getwd()
setwd()

dir.create("data")
dir.create("data_output")
dir.create("fig_output")


download.file(
  "https://raw.githubusercontent.com/datacarpentry/r-socialsci/main/episodes/data/SAFI_clean.csv",
  "data/SAFI_clean.csv", mode = "wb"
  )

# what is code?
    # code is written instructions
    # execution
    # write in console or editor (reproducible)
    # CMD+enter; 'run' buttons
    # control+1 / control+2
    # Typing in console: 
        # > 
        # + 
        # [nothing]

# library/package, pre-written code
    # CRAN
    # how to install (packages tab/installed.packages()/install.packages())
    # EXERCISE: make sure you have the following package installed: tidyverse
        # (includes ggplot2, dplyr)

install.packages("tidyverse")















