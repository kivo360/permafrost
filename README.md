# Permafrost

`Permafrost` is a library that gets emails by the company name, verifies if the email exist, then creates a csv file in the current location.

You can do this entirely from your command line. You need to enter the name of the person you're looking for.


This should return a list of emails about bill gates. Bill Gates will probably be filtered if you try to email him.
```bash
permafrost --save True --debug True names bill gates microsoft.com
```


## How to install
Install using `pip3`.

```bash
pip3 install permafrost
```


---


## **Key Settings**

**Optional Parameters**

* `--save` - a bool set to save the results. `True` if you're looking to save it. Set to `False` by default. `-s` for short.
* `--debug` - Print all of the emails that exist within the domain. Set to `False` by default. `-d` for short.
* `--middle` - The `middle` name of the person you're looking for. This is completely optional. `-m` for short.


This should give us everything for bill henry gates @ microsoft.com
```bash
permafrost -s True -d True names bill gates microsoft.com -m henry
```



**Parameters**

```
permafrost names [first] [last] [domain]
```

* `first` - The first name of the person you're looking for.
* `last` - The last name of the person you're looking for.
* `domain` - The domain name you're searching through. 

