# let template.root or similar be something that knows the source data layout of the file we are going to look at.

from template.root import evt_model, pt, met

events = evt_model.load('gridds:mybogusdatsetname')

good_jets = pt > 40

plt.hist(events[met > 100].jets[good_jets].pt)
