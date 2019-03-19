# Cut and plot on a distribution

good_events = events[met > 60]

plt.hist(good_events.met, bins=50)


# Alternate way, using the LINQ version, but should be equivalent.
events.Where(lambda e: e.met > 60).PlotHisto(bins=50)
