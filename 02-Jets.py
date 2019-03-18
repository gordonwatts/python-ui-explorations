# Look at jet collections in the data

# A proxy for all the jets.
all_jets = events.jets

# A good jet is one that has pt greater than 40 GeV
a_good_jet = pt > 40
good_jets = all_jets[a_good_jet]

# Events with at least 2 good jets
good_events = events.jets[len(good_jets) >= 2]

# Plot the pT of all jets that are in good events.
plt.hist(good_events.jets.pt)

# Plot the pT of all good jets in good events.
plt.hist(good_events.jets[a_good_jet].pt)
