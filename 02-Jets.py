# Look at jet collections in the data

# A proxy for all the jets.
all_jets = events.jets

# A good jet is one that has pt greater than 40 GeV
a_good_jet = all_jets.pt > 40
good_jets = all_jets[a_good_jet]

# Events with at least 2 good jets
good_events = events[events.jets[len(good_jets) >= 2]]

# Plot the pT of all jets that are in good events.
plt.hist(good_events.jets.pt)

# Plot the pT of all good jets in good events.
plt.hist(good_events.jets[a_good_jet].pt)

# Alternate way, with LINQ

a_good_jet = lambda j: j.pt > 40

good_events = events \
                .Where(lambda e: e.jets.where(lambda j: a_good_jet(j)).count() > 2)

good_events.SelectMany(lambda e: e.jets) \
        .Select(lambda j: j.pt) \
        .Plot(bins=50)

good_events.SelectMany(lambda e: e.jets) \
        .Where(lambda j: a_good_jet(j)) \
        .Select(lambda j: j.pt) \
        .Plot(bins=50)
