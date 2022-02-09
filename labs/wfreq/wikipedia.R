load("wikipedia_cut200.RR")
hist(wfreq[wfreq < 10000])
plot(wfreq, log = "xy")