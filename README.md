dni2name
===============

Returns a name from a DNI number using Google this way:
```
julian@garden-of-eden:~/git/dni2name$ python dni2name.py 33779884
33779884 Esteban Roitberg
```

dni2name searchs in google for the query: "DNI input-number" and the extract the full name from the title using only two hand written rules.
The file dni2name.py contains the code that does this. I commented it a lot so it's understandable for people that knows only a little of programming. The language used is python. (''' The text between three quotes is a comment. ''' and the rest is the code).

##Usage

**Clone and use**
```
julian@garden-of-eden:~/git$ git clone git@github.com:julian3833/dni2name.git
julian@garden-of-eden:~/git$ cd dni2name
```

**Run Esteban Roitberg test**
```
julian@garden-of-eden:~/git/dni2name$ python dni2name.py
33779884 Esteban Roitberg

```

**Check for a DNI number**
```
julian@garden-of-eden:~/git/dni2name$ python dni2name.py 33799335
33799335 Angeletti Julieta Belen
```

**Check for a range of DNIs**
```
julian@garden-of-eden:~/git/dni2name$ python dni2name.py 33779900 33779910
33779902 Lacalle Juan Manuel
33779903 Fernandez Leon Maria Alejandra
33779904 Zippes Alan Ezequiel
33779905 Capon Laura Mariela
33779907 Brasa Lucia
33779908 Martin Gusta Bascary
33779909 Guerrero Sandra Ines

```

##Dependencies

**This git repo**

Uses this library: https://github.com/BirdAPI/Google-Search-API. The files are included for simplicity.  

```
git clone https://github.com/BirdAPI/Google-Search-API.git GoogleSearchAPI/
```

**Enviroment**

You need a Linux and I think that's all.

Install git and python. It's something like this:
```
apt-get install git python
```

Google it.
