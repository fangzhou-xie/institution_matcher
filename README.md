# institution_matcher

Match Institution Name to [GRID](https://www.grid.ac/downloads) dataset.

Use [Fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy) package.

currently support exact matching only

TODO: fuzzy match of institution name as well

Usage:

    >>> im = InstitutionMatcher()
    >>> im.match('Stanford University')
    ('grid.168010.e', 'Stanford University', 'Stanford', 'California', 'United States')
