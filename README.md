# WDay (Whirl Data, alternative to YAML)

[![Downloads](https://pepy.tech/badge/wday/month)](https://pepy.tech/project/wday/month)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/Whirlpool-programmer/wday.svg)](https://github.com/whirlpool-programmer/wday/blob/master/LICENSE)
[![CodeFactor](https://www.codefactor.io/repository/github/whirlpool-programmer/wday/badge)](https://www.codefactor.io/repository/github/whirlpool-programmer/wday)

## A simple Data storage alternative to json and yaml

## How to use?
You just call the module by the read() function to read the data..

example:
```python3
>>> import wday
>>> data = 'Windows::['v11'::{'quality':['best','great']}]'
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
> Commented lines start with '\~' and there is no inline comment as of now

4. What is the line beginning with `@`?
> that is a remark..

EXAMPLE DATA:
```
~ this is a comment as you know...
wday::["v1"::{"by":"Whirlpool programmer"}]

~ EXAMPLE 2:
~ Python File runner as configured in WhirlEdit 2.0 by default:
Python::[".py"::"python $file"]
```

# Special Function `script()`:

So.. There is a special function called "script()"
which makes wday a language..

in script, you give it a script which it runs..
it has its own specific rules..

1. every line has to end in ';'
2. example `if..else..` statement:
   ```
   if (name=="hello"):
       console.put('is "hello" a name?!');
   ```
3. to use a variable from outside of a function, it should be made `global variable`..

example:
```
@config.theme
Themefolder::['./Themes/']
DefaultTheme::['azure-dark.whTheme']

@config.scheme/highlight
Schemefolder::['$default']
DefaultScheme::['azure']

@config.font
Font::['Consolas'::12]

'''
def function(*args):
	global entry;
	global name;
	if (entry.get() == "windows"):
		console.put('hello MS-Windows!');
		name.set('MS-Windows');
	else:
		console.put('hi..');

name = StringVar();
name.set('none..');
entry = gui.Entry(window);
entry.grid();
btn = gui.Button(window,text="check?",command = function);
btn.grid();
label = gui.Label(window,textvariable = name);
label.grid();
window.mainloop();
'''
```
As you can see..
It also has gui functionalities.. inspired from Tkinter..
and remember..
the main data of the file is stored in a variable called `init`..
so you can use this program too:

```
Whirledit::['v1'::'v2'::'v3']

'''
#HERE STARTS THE PROGRAM!
console.put(init);
# as you remember, init is the data..
'''
```
OUTPUT:
`{'@': [], "Whirledit":['v1', 'v2', 'v3']}`

## who's using it?
> well... probably nobody.. just me.. in my project WhirlEdit (i wrote this in previous versions!)
> I have been proven wrong!!
> just look at this: [![Downloads](https://pepy.tech/badge/wday/month)](https://pepy.tech/project/wday/month)
