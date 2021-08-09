# WDay (Whirl Data, alternative to YAML)

[![Downloads](https://pepy.tech/badge/wday/month)](https://pepy.tech/project/wday/month)

## A simple Data storage alternative to json and yaml

## How to use?
You just call the module by the read() function to read the data..

example:
```python3
>>> import wday
>>> data = Windows::['v11'::{'quality':['best','great']}]
>>> print(wday.read(data))
{'Windows': ['v11', {'quality': ['best', 'great']}]}
```

## DOCS for WDay:

### there's not much to learn here.. just look at the simple syntax

```
Name::[value1::[list_item_1,list_item_2]::{dictonary_key_1:dictonary_key_1_value}]
```
That's soooo simple!

1. But what is the separator as an alternative to comma ","?
> the "::" that you can see is the separator for the data values..

2. What if my data has square brackets? or "::"?
> that's simple use a \:: in place of "::" and \[, \] in place of "[" or "]"

3. what about comments?
> Commented lines start with "~" and there is no inline comment as of now..

EXAMPLE DATA:
```
~ this is a comment as you know...
wday::["v1"::{"by":"Whirlpool programmer"}]

~ EXAMPLE 2:
~ Python File runner as configured in WhirlEdit 2.0 by default:
Python::[".py"::"python $file"]
```

## who's using it?
well... probably nobody.. just me.. in my project WhirlEdit
