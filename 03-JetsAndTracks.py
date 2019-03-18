# Look at tracks connected to jets.

# OK jets and tracks
ok_jets = events.jets[pt > 40]
good_tracks = events.tracks[pt > 1.0]

# A good jet is one that has at least 2 tracks within a delta-R of 0.2
# DR is a function that calculates the opening angle (eta, phi). p3 is a 3-vector that
# knows how to get eta and phi, which DR does under the covers for this example
# This might be, in reality, ugly, note the "tracks_near_jets" is in the context of each jet - only those tracks
#   near the jet being considered are counted in the second line here.
tracks_near_jets = good_tracks[DR(p3,ok_jets.p3)<0.2]
good_jets = ok_jets[len(tracks_near_jets) >= 2]

# Plot the pT of good jets
plt.hist(good_jets.pt)

# Plot the tracks near a good jet
plt.hist(tracks_near_jets.pt)
plt.hist(tracks_near_jets.eta)
