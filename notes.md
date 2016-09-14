# Notes

This is a brief list of examples. See the documentation for details.

```python
# most recent
h = db[-1]

# what is a header

db.get_table(h)

# more ways to get headers....

# all
db()

# using length measure number of results
len(db())

len(db(plan_name='scan'))
len(db(detectors='det'))
len(db(motors='motor'))

# and
len(db(motors='motor', proposal_id=1))

# arbitrary fields
len(db(operator='Ken'))

# filters
db.add_filter(proposal_id=1)
len(db())
len(db(plan_name='count'))

db.filters
db.clear_filters()

# alias
db.alias('prop3', proposal_id=3)

# advanced MongoDB query example
len(db(operator={'$exists': True}))
```
