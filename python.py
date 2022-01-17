Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> \]
SyntaxError: unexpected character after line continuation character
>>> type(3)
<class 'int'>
>>> ttype(73.81)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    ttype(73.81)
NameError: name 'ttype' is not defined
>>> type(73.81)
<class 'float'>
>>> type("hello world")
<class 'str'>
>>> type("")
<class 'str'>
>>> type(" ")
<class 'str'>
>>> type('True')
<class 'str'>
>>> 8%10
8
>>> 8/10
0.8
>>> 8//10
0
>>> 4**8
65536
>>> 1.5+2*3
7.5
>>> 16-3/2+7-1
20.5
>>> 5.3**3%5
3.876999999999981
>>> 3//2
1
>>> 10//3
3
>>> 100//23
4
>>> 8//5-3
-2
>>> counties = ["Arapahoe","Denver","Jefferson"]
>>> counties
['Arapahoe', 'Denver', 'Jefferson']
>>> counties(0)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    counties(0)
TypeError: 'list' object is not callable
>>> counties[0]
'Arapahoe'
>>> len(counties)
3
>>> counti3es.append("el paso")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    counti3es.append("el paso")
NameError: name 'counti3es' is not defined
>>> counties.append("El Paso")
>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> counties.pop(3)
'El Paso'
>>> counites
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    counites
NameError: name 'counites' is not defined
>>> counties
['Arapahoe', 'Denver', 'Jefferson']
>>> counties.insert(2, El Paso)
SyntaxError: invalid syntax
>>> counties.insert(2, EL Paso)
SyntaxError: invalid syntax
>>> counties.insert(2, "El Paso")
>>> counties.remove("Arapahoe")
>>> counties
['Denver', 'El Paso', 'Jefferson']
>>> counties.append("Denver")
>>> counties.remove("Denver")
>>> counties
['El Paso', 'Jefferson', 'Denver']
>>> counties.append("Arapahoe")
>>> counties
['El Paso', 'Jefferson', 'Denver', 'Arapahoe']
>>> counties_dict = {}
>>> counties_dict["Arapahoe"] = 422829
>>> counties_dict
{'Arapahoe': 422829}
>>> counties_dict["denver"] = 463353
>>> counties_dict["Jefferson"]=432438
>>> counties_dict
{'Arapahoe': 422829, 'denver': 463353, 'Jefferson': 432438}
>>> len(counties_dict)
3
>>> counties_dict.items()
dict_items([('Arapahoe', 422829), ('denver', 463353), ('Jefferson', 432438)])
>>> counties_dict.keys()
dict_keys(['Arapahoe', 'denver', 'Jefferson'])
>>> counties_dict.values
<built-in method values of dict object at 0x000002016E179278>
>>> counties_dict.values()
dict_values([422829, 463353, 432438])
>>> counties_dict.get("denver")
463353
>>> counties_dict["arapahoe")
SyntaxError: invalid syntax
>>> counties_dict["arapahoe"]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    counties_dict["arapahoe"]
KeyError: 'arapahoe'
>>> counties_dict["Arapahoe"]
422829
>>> voting_data = []
>>> voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
>>> voting_data.append({"county":"Denver", "registered_voters": 463353})
>>> voting_data.append({"county":"Jefferson", "registered_voters": 432438})
SyntaxError: multiple statements found while compiling a single statement
>>> voting_data.append({"county":"Arapahoe", "registered_voters": 422829})

>>>  voting_data.append({"county":"Denver", "registered_voters": 463353})
 
>>> voting_data.append({"county":"Jefferson", "registered_voters": 432438})
SyntaxError: unexpected indent
>>> 
>>> 
>>> voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}]
>>> voting_data.append({"county":"Denver", "registered_voters": 463353})
>>> voting_data.append({"county":"Jefferson", "registered_voters": 432438})
>>> voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
>>> voting_data.insert(2, {"county":"El Paso", "registered_voters": 461149})
>>> voting_data.Remove({"county":"Arapahoe", "registered_voters": 422829})
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    voting_data.Remove({"county":"Arapahoe", "registered_voters": 422829})
AttributeError: 'list' object has no attribute 'Remove'
>>> voting_data.remove({"county":"Arapahoe", "registered_voters":422829})
>>> voting_data
[{'county': 'Denver', 'registered_voters': 463353}, {'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}]
>>> voting_data.remove({"county":"denver", "registered_voters":463353})
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    voting_data.remove({"county":"denver", "registered_voters":463353})
ValueError: list.remove(x): x not in list
>>> voting_data.remove({"county":"Denver", "registered_voters":463353})
>>> voting_data.append({"county":"Denver", "registerd_voters":463353})
>>> voting_data.append({"county":"Arapahoe", "registered_voters":4422829})
>>> voting_data
[{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'Denver', 'registerd_voters': 463353}, {'county': 'Arapahoe', 'registered_voters': 4422829}]
>>> 