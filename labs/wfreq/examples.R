v <- c(1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 5, 5, 5, 6)
# histogram
hist(v)
hist(v, breaks = 10) # 10 bins
# histogram of 1000 number sample following uniform distribution
hist(runif(1000))
# histogram of 2000 number sample following normal distribution (mean 4, sd 1)
hist(rnorm(2000, 4, 1))
# load vector from file
source("simple.R")
hist(v2)