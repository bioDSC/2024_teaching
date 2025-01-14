
################################################################################
# Episode 6: Data Visualisation with ggplot2
# https://datacarpentry.github.io/r-socialsci/05-ggplot2.html
################################################################################

# THIS EPISODE
# - using yesterday's data
# - we'll be looking into multiple ways of plotting data

library(tidyverse)
library(ggplot2)

# interviews_plotting <- read_csv("data_output/interviews_plotting.csv")
interviews_plotting <- readRDS("data_output/interviews_plotting.rds")

# Cheat sheet:
# https://raw.githubusercontent.com/rstudio/cheatsheets/main/data-visualization.pdf

###

# Very simple plotting in base R
# Useful, but not very advanced

plot(interviews_plotting$no_membrs, interviews_plotting$liv_count,
     main = "Base R Scatterplot",
     xlab = "Number of Household Members",
     ylab = "Number of Livestock Owned")


###

# !! SKIP this "lattice" !!
# Another example of a plotting system

library(lattice)

xyplot(liv_count ~ no_membrs | village, data = interviews_plotting,
       main = "Lattice Plot: Livestock Count by Household Members",
       xlab = "Number of Household Members",
       ylab = "Number of Livestock Owned")

###

# general template

# <DATA> %>%
#     ggplot(aes(<MAPPINGS>)) +
#     <GEOM_FUNCTION>()


interviews_plotting %>%
    ggplot(aes(x = no_membrs, y = number_items)) +
    geom_point()




###

# Assign plot to a variable
interviews_plot <- interviews_plotting %>%
    ggplot(aes(x = no_membrs, y = number_items))

# Draw the plot as a dot plot
plot1 <- interviews_plot +
            geom_point()
plot1

# Addition MW
# Allows you to choose something else easily
plot2 <- interviews_plot +
            geom_density_2d(bins=7)
plot2


###

# so we have
interviews_plotting %>%
    ggplot(aes(x = no_membrs, y = number_items)) +
    geom_point()

# plot not optimal
# but points are hidden

# we can change properties
interviews_plotting %>%
    ggplot(aes(x = no_membrs, y = number_items)) +
    geom_point(alpha = 0.5)


# perhaps "jitter"?
# (adds random displacement)
interviews_plotting %>%
    ggplot(aes(x = no_membrs, y = number_items)) +
    geom_jitter()


# MW: this is (almost) data manipulation

# so we want less displacement; use parameters of the geom_jitter function
interviews_plotting %>%
    ggplot(aes(x = no_membrs, y = number_items)) +
    geom_jitter(alpha = 0.5,
                width = 0.2,
                height = 0.2)

# can also change color
interviews_plotting %>%
    ggplot(aes(x = no_membrs, y = number_items)) +
    geom_jitter(alpha = 0.5,
                color = "blue",
                width = 0.2,
                height = 0.2)


# and also highlight villages
interviews_plotting %>%
    ggplot(aes(x = no_membrs, y = number_items)) +
    geom_jitter(aes(color = village), alpha = 0.5, width = 0.2, height = 0.2)


# (still not really optimal --> later improvement)


# "note"
# they give an alternative option, which already looks a bit better
interviews_plotting %>%
   ggplot(aes(x = no_membrs, y = number_items, color = village)) +
   geom_count()

    # addition MW
    # always keep in mind, we can use help function
    ?geom_count


###

################################################################################

# Exercise
# 
# Use what you just learned to create a scatter plot of rooms by village with 
# the respondent_wall_type showing in different colours. Does this seem like a 
# good way to display the relationship between these variables? 
# What other kinds of plots might you use to show this type of data?


# <GO OVER SOLUTION TOGETHER>





# my solution
interviews_plotting %>%
   ggplot(aes(x = village, y = rooms, color = respondent_wall_type)) +
   geom_point()

interviews_plotting %>%
    ggplot(aes(x = village, y = rooms)) +
    geom_jitter(aes(color = respondent_wall_type),
      alpha = 0.5,
        width = 0.2,
        height = 0.2)

# "This is not a great way to show this type of data 
# because it is difficult to distinguish between villages. 
# What other plot types could help you visualize this 
# relationship better?"


################################################################################

# Another convenient display is the boxplot
interviews_plotting %>%
    ggplot(aes(x = respondent_wall_type, y = rooms)) +
    geom_boxplot()

# - allows quick comparison summary param
    # - e.g. mean, width distr
    # muddaub houses tend to be smaller
# - doesn't show all features --> add points

interviews_plotting %>%
    ggplot(aes(x = respondent_wall_type, y = rooms)) +
    geom_boxplot(alpha = 0) +
    geom_jitter(alpha = 0.5,
        color = "tomato",
        width = 0.2,
        height = 0.2)+
    theme_bw() # addition MW, don't forget to mention google!!


# how can we switch the order of the layers? And make the boxplots on top?
interviews_plotting %>%
    ggplot(aes(x = respondent_wall_type, y = rooms)) +
    geom_jitter(alpha = 0.5,
        color = "tomato",
        width = 0.2,
        height = 0.2)+
    geom_boxplot(alpha = 0) +
    theme_bw() # addition MW, don't forget to mention google!!


################################################################################

# Exercise
# 
# (A)
# Boxplots are useful summaries, but hide the shape of the distribution. 
# For example, if the distribution is bimodal, we would not see it in a boxplot. 
# An alternative to the boxplot is the violin plot, where the shape 
# (of the density of points) is drawn.
# 
# Replace the box plot with a violin plot; see geom_violin().
# 
# 
# (B)
# So far, we’ve looked at the distribution of room number within wall type. 
# Try making a new plot to explore the distribution of another variable within wall type.
# 
# Create a boxplot for liv_count for each wall type. Overlay the boxplot layer 
# on a jitter layer to show actual measurements.
# 
# 
# (C)
# Add colour to the data points on your boxplot according to whether the respondent 
# is a member of an irrigation association (memb_assoc).

# <GO OVER SOLUTIONS TOGETHER>





# My solutions
# (A)
interviews_plotting %>%
    ggplot(aes(x = respondent_wall_type, y = rooms)) +
    geom_jitter(alpha = 0.5,
        color = "tomato",
        width = 0.2,
        height = 0.2)+
    geom_violin(alpha = 0) +
    theme_bw() # addition MW, don't forget to mention google!!

# (B) 
# Create a boxplot for liv_count for each wall type. Overlay the boxplot layer 
# on a jitter layer to show actual measurements.
interviews_plotting %>%
    ggplot(aes(x = respondent_wall_type, y = liv_count)) +
    geom_jitter(alpha = 0.5,
        width = 0.2,
        height = 0.2, mapping = aes(color = memb_assoc)
        )+
    geom_boxplot(alpha = 0) +
    theme_bw()
# (C)
interviews_plotting %>%
    ggplot(aes(x = respondent_wall_type, y = liv_count)) +
    geom_jitter(alpha = 0.5,
        width = 0.2,
        height = 0.2, mapping = aes(color = memb_assoc)
        )+
    geom_violin(alpha = 0) +
    theme_bw()



################################################################################

# bar plot

# - per default, acts like a histogram
#       - counts the number of instances each value apears in the dataset

interviews_plotting %>%
    ggplot(aes(x = respondent_wall_type)) +
    geom_bar()


# fill can be used to inspect further features in the data
# e.g. proportion of each
interviews_plotting %>%
    ggplot(aes(x = respondent_wall_type)) +
    geom_bar(aes(fill = village))

# difficult te read

# to create side-by side bars, use:

# position="dodge" 
interviews_plotting %>%
    ggplot(aes(x = respondent_wall_type)) +
    geom_bar(aes(fill = village), position = "dodge")

# interesting, 

# However, more interested in proportion of houses
# So normalize to villages

# Calculation to create new parameter


percent_wall_type <- interviews_plotting %>%
    # remove cement as there was only one
    filter(respondent_wall_type != "cement") %>%
    # count (remember, effectively count = group.by + n())
    ## View(percent_wall_type)
    count(village, respondent_wall_type) %>%
    # now, per village, calculate percentages
        # note that n was calculated before (show intermediate result)
    group_by(village) %>%
    mutate(percent = (n / sum(n)) * 100) %>%
    ungroup() # important!

# View(percent_wall_type)

# now we can plot this
percent_wall_type %>%
    ggplot(aes(x = village, y = percent, fill = respondent_wall_type)) +
    geom_bar(stat = "identity", position = "dodge")+
        # MW: note that here we use 'stat = "identity"', 
            # - default = count; which counts similar instances
            # - stat='identity' telling ggplot to use data 'as is'
    theme_bw()


################################################################################

# Exercise
# 
# Create a bar plot showing the proportion of respondents in each village who are
# or are not part of an irrigation association (memb_assoc). Include only respondents 
# who answered that question in the calculations and plot. Which village had the 
# lowest proportion of respondents in an irrigation association?


# <GO OVER SOLUTION TOGETHER>







# proportion of respondents memb_assoc / village, remove NA
percent_memb_assoc <- interviews_plotting %>% 
    filter(!is.na(memb_assoc)) %>% 
    count(memb_assoc, village) %>% 
    # calculate percentages
    group_by(village) %>% 
    mutate(percentage_n = n/sum(n)*100) %>% 
    ungroup()

percent_memb_assoc %>%
   ggplot(aes(x = village, y = percentage_n, fill = memb_assoc)) +
    geom_bar(stat = "identity", position = "dodge")+
    theme_bw()
    # --> Ruaca lowest proportion assoc members
    


################################################################################
# labels and titles

# add labels (labs)
percent_wall_type %>%
    ggplot(aes(x = village, y = percent, fill = respondent_wall_type)) +
    geom_bar(stat = "identity", position = "dodge") +
    labs(title = "Wall types",
         subtitle = "proprtion per village",
         fill = "Type of Wall in Home", # can refer to any aesthetic in the plot
         x = "Village",
         y = "Percent",
         caption = "Caption text")

# Often, convenient to subdivide data in multiple plots
# facet_wrap

percent_wall_type %>%
    ggplot(aes(x = respondent_wall_type, y = percent)) +
    geom_bar(stat = "identity", position = "dodge") +
    labs(title="Proportion of wall type by village",
         x="Wall Type",
         y="Percent") +
    facet_wrap(~ village)+ # note: ~ is a "formula"
    #facet_grid(cols = vars(village))+ # MW
    #facet_grid(rows = vars(village))+ # MW
    theme_bw()+
    theme(panel.grid = element_blank())

# same for number of items 

# calculate percentages of items

# let's build this up slowly

# completely manual
# number of entries for town
nrow(interviews_plotting[interviews_plotting$village=='Chirodzo',])
# number of entries having bicycle (True)
sum(interviews_plotting[interviews_plotting$village=='Chirodzo',]$bicycle)
# percentage
17 / 39 * 100

# now for one column
interviews_plotting %>%
    # need two columns
    select(bicycle, village) %>% 
    # per village
    group_by(village) %>%
    # calculation as above
    # (summarize calculates summary parameter you define)
    summarize(sum(bicycle) / n() * 100) 

# convenient to do this for multiple columns at once

# the same as above can be done, 
# using across,
# allows _applying same transformation to multiple columns_
percent_items <- interviews_plotting %>%
    group_by(village) %>%
    summarize(across(bicycle:no_listed_items, ~ sum(.x) / n() * 100)) %>%
        # across:
        # [across multiple columns]
        # see also ?across
        # arg 1: columns
        # arg 2: function
        #           ~, tilda or twiddle, indicates definition of formula
        #               technical note to self: ~ takes a vector and translates it to formula, where .x is input vector
        #               as_mapper(~ sum(.x) / n() * 100)
        #               https://adv-r.hadley.nz/functionals.html
        #           .x, input vector
        #           -   can use function definition as well, more clear,
        #               however, "~" notation is often used
        #
        # technical note to self:
        # equals:
        #summarize(across(bicycle:no_listed_items, function(x) { sum(x) / length(x) * 100} )) %>%
    ## View(percent_items)
    # Wide format is not understood plotting, so we need to pivot
    pivot_longer(bicycle:no_listed_items, names_to = "items", values_to = "percent")

# now we can plot again
# using things we learned before
percent_items %>%
    ggplot(aes(x = village, y = percent)) +
    geom_bar(stat = "identity", position = "dodge") +
    facet_wrap(~ items) +
    theme_bw() +
    theme(panel.grid = element_blank())
    # Addition MW, also shown later
    #, axis.text.x = element_text(angle = 90))

################################################################################

# 

################################################################################

# Exercise
# 
# Experiment with at least two different themes. Build the previous plot using 
# each of those themes. Which do you like best?
#
# For an overview, see:
# https://ggplot2.tidyverse.org/reference/ggtheme.html
# 
# From Carpentries text:
# "theme_minimal() and theme_light() are popular, and theme_void() can be useful"
# For extensions to ggplot, see also:
# https://exts.ggplot2.tidyverse.org/
#
# <GO OVER ANSWERS TOGETHER>




# solution
# see
# https://ggplot2.tidyverse.org/reference/ggtheme.html
#
# - which one did you try?

################################################################################

# input from ppl:
# how would you improve the plot?


# improvements suggested carpentries:



percent_items %>%
    ggplot(aes(x = village, y = percent)) +
    geom_bar(stat = "identity", position = "dodge") +
    facet_wrap(~ items) +
    # better labels,
    # \n indicates a new line
    labs(title = "Percent of respondents in each village \n who owned each item",
         x = "Village",
         y = "Percent of Respondents") +
    theme_bw() +
    theme(
        # increased font size
        text = element_text(size = 16),
        # axis text changes
        axis.text.x = element_text(colour = "grey20", size = 12, angle = 45,
                                      hjust = 0.5, vjust = 0.5),
        axis.text.y = element_text(colour = "grey20", size = 12)
        )

# "Note that it is also possible to change the fonts of your plots. 
# If you are on Windows, you may have to install the extrafont package, 
# and follow the instructions included in the README for this package."

# can define a theme beforehand, 
# and apply to multiple plots 
# (or increase readability)
grey_theme <- theme(axis.text.x = element_text(colour = "grey20", size = 12,
                                               angle = 45, hjust = 0.5,
                                               vjust = 0.5),
                    axis.text.y = element_text(colour = "grey20", size = 12),
                    text = element_text(size = 16),
                    plot.title = element_text(hjust = 0.5))


percent_items %>%
    ggplot(aes(x = village, y = percent)) +
    geom_bar(stat = "identity", position = "dodge") +
    facet_wrap(~ items) +
    labs(title = "Percent of respondents in each village \n who owned each item",
         x = "Village",
         y = "Percent of Respondents") +
    grey_theme


################################################################################


# Exercise
# 
# With all of this information in hand, please take another five minutes to either 
# improve one of the plots generated in this exercise or create a beautiful graph 
# of your own. Use the RStudio ggplot2 cheat sheet for inspiration. 
# 
# Here are some ideas:
# - See if you can make the bars white with black outline.
# - Try using a different colour palette (see http://www.cookbook-r.com/Graphs/Colors_(ggplot2)/).
# 
# Addition MW:
# Color blind friendly palette (see also link above, A colorblind-friendly palette): 
# - https://davidmathlogic.com/colorblind/#%23D81B60-%231E88E5-%23FFC107-%23004D40
# - https://www.nature.com/articles/nmeth.1618
# - https://personal.sron.nl/~pault/



# <GO OVER SOME SUGGESTIONS>



# making bars white/black
percent_items %>%
    ggplot(aes(x = village, y = percent)) +
    geom_bar(stat = "identity", position = "dodge", color='black', fill='white') +
    facet_wrap(~ items) +
    labs(title = "Percent of respondents in each village \n who owned each item",
         x = "Village",
         y = "Percent of Respondents") 
    #+ grey_theme 
    



################################################################################

# Saving your plot

# Choose a convenient format
# pdf, svg --> editable later

# Save yourself some time
    # Save to the right dimensions
    # Save with the right font face and size

my_plot <- percent_items %>%
    ggplot(aes(x = village, y = percent)) +
    geom_bar(stat = "identity", position = "dodge") +
    facet_wrap(~ items) +
    labs(title = "Percent of respondents in each village \n who owned each item",
         x = "Village",
         y = "Percent of Respondents") +
    theme_bw() +
    theme(axis.text.x = element_text(color = "grey20", size = 12, angle = 45,
                                     hjust = 0.5, vjust = 0.5),
          axis.text.y = element_text(color = "grey20", size = 12),
          text = element_text(size = 16),
          plot.title = element_text(hjust = 0.5))

ggsave("fig_output/myplot.png", my_plot, width = 15, height = 10)

# addition MW:
# standard publication format = 17.2 cm wide
martijntheme <- theme(#legend.position="none",
          text = element_text(size=8, family='Arial'),
          axis.text = element_text(size=8, family='Arial'),
          plot.title = element_text(size=8, family='Arial'))

my_plot_martijn <- my_plot + martijntheme

dir.create('fig_output')
ggsave('fig_output/myplot.pdf', my_plot, width=5, height =5, units = 'cm', device=cairo_pdf, dpi=600)
    # this is for macbook! (not sure advice applies windows)
    # earlier note carpentries:
        # "Note that it is also possible to change the fonts of your plots. 
        # If you are on Windows, you may have to install the extrafont package, 
        # and follow the instructions included in the README for this package."

# compare with png version!


# addition MW (just for show!)
interviews_plotting %>%
   ggplot(aes(x = no_membrs, y = number_items, color = village)) +
   geom_density_2d(bins=6)+
    facet_grid(cols = vars(village))

# Take home points

# - The data set and coordinate system can be defined using the ggplot function.
# - Additional layers, including geoms, are added using the + operator.
# - Many types of plots --> use google/other resources to suit your needs (edit MW)
# - Faceting allows you to generate multiple plots based on a categorical variable.










