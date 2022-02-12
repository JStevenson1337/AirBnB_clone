# AirBnB Clone
In this project we will implement AirBnB clone using console.

## Usage
The shell should work like this in interactive mode:
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  exit  help  quit  show  update

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
It can be also used in non-interactive mode:

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  exit  help  quit  show  update
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================

EOF  all  count  create  destroy  exit  help  quit  show  update
(hbnb) 
$
```


## Basic usage

| Command | Syntax | Return |
|---------|--------|--------|
| help | `help` or `help <command>` | Returns list of commands |
| quit | `quit` | Quits the prompt |
| exit | `exit` | Same as `quit` |
| EOF | End Of File | Exit prompt with `ctrl + D` |
| create | `create <class>` | Creates a new class instance |
| all | `all` or `all <class>` | Shows all instances of a class |
| show | `show <class> <id>` | Shows an instance of a class if it exists |
| update | `<class> <id> <attr. name> <attr. value>` | Updates a class attribute with a value |
| destroy | `destroy <class> <id>` | Deletes a class instance |


## Examples 

```
    (hbnb) help
    Documented commands (type help <topic>):
    ========================================
    EOF  all  count  create  destroy  exit  help  quit  show  update

    (hbnb)
```

```
    (hbnb) create
    ** class doesn't exist **
    (hbnb) create BaseModel
    BaseModel.[BaseModel] (6b028b85-0cf8-481b-a91f-63aa7f6eed58) {'id': '6b028b85-0cf8-481b-a91f-63aa7f6eed58', 'created_at': datetime.datetime(2022, 2, 11, 23, 4, 20, 528736), 'updated_at': datetime.datetime(2022, 2, 11, 23, 4, 20, 528739)}
    (hbnb) 
```

```
    (hbnb) all
    {...'BaseModel.6b028b85-0cf8-481b-a91f-63aa7f6eed58': <models.base_model.BaseModel object at 0x7f72ca231e20>}
    (hbnb)
```

```
    (hbnb) show
    ** class doesn't exist **
    (hbnb)
    (hbnb) show BaseModel
    ** instance id missing **
    (hbnb)
    (hbnb) show BaseModel 6b028b85-0cf8-481b-a91f-63aa7f6eed58
    ** class doesn't exist **
    (hbnb) 
```
