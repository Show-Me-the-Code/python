Some mention about a detail
===

If you regard 'They're' as two words and don't need to find numbers, just use `[a-zA-Z]+\b` is enough.

Well, the way to distinguish ' from `\b` that I think up is to write re like this: `[a-zA-Z]+('[a-zA-Z]+|\b)`

The order is very important, if you write `[a-zA-Z]` after `|` , it will be ignore. 

What's more, in python use `'` in a string `\'` is necessary.

	re.findall(r'[a-zA-Z]+(\'[a-zA-Z]+|\b)',string) 


---

##Warning##

There are some mistake use this re in Python. It works well in Sublime. I will try to fix it in several days. Thank you! 