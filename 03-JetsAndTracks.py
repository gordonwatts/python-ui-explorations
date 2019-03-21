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


# Using the LINQ approach
a_ok_jet = lambda j: j.pt > 40
a_good_track = lambda t: t.pt > 1.0

# I'm using a tuple here, but being able to "create" a named object here is very helpful.
good_jets = events \
                .SelectMany(lambda e: e.jets.Select(lambda j: (j, e.tracks.where(lambda t: DR(t.p3, j.p3) < 0.2)))) \
                .Where(lambda info: info[1].count() >= 2)

# Plot the jet pT
good_jets \
        .select(lambda j: j[0].pt) \
        .Plot(nbins=50, title = 'Good jet ')

# Plot the tracks near a good jet
good_tracks = good_jets \
                .SelectMany(lambda info: info[1])

good_tracks.select(lambda t: t.pt).Plot(nbins=50, title = 'Good track pt')
good_tracks.select(lambda t: t.eta).Plot(nbins=50, title = 'Good track eta')
