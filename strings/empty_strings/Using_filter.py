                       "Using filter() method"

"""Using filter() is the most elegant and fastest way to perform this task. 
This method is highly recommended because speed matters when we deal with
    large machine learning data set that may potentially contain empty string."""

pratik=["",'name','','asiod']
prat=list(filter(None,pratik))
print(prat)
