Description: The project aims to build the first stage to complete web application that is a clone of the famous AirBnB. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions. 

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
f68116faa1f14c3584611698f0cf17fe
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel f68116faa1f14c3584611698f0cf17fe
[BaseModel] (f68116faa1f14c3584611698f0cf17fe) {'id': 'f68116faa1f14c3584611698f0cf17fe', 'created_at': datetime.datetime(2024, 3, 30, 17, 57, 43, 200462), 'updated_at': datetime.datetime(2024, 3, 30, 17, 57, 43, 200491)}
(hbnb)
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel f68116faa1f14c3584611698f0cf17fe
(hbnb) show BaseModel f68116faa1f14c3584611698f0cf17fe
** no instance found **
(hbnb)
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```

(hbnb) update BaseModel 5ef098ee9f214f1db9ed226634080cb9 first_name "John"
(hbnb) show BaseModel 5ef098ee9f214f1db9ed226634080cb9
[BaseModel] (5ef098ee9f214f1db9ed226634080cb9) {'id': '5ef098ee9f214f1db9ed226634080cb9', 'created_at': datetime.datetime(2024, 3, 30, 18, 0, 58, 145321), 'updated_at': datetime.datetime(2024, 3, 30, 18, 0, 58, 145342), 'first_name': 'John'}
(hbnb)
```
###### Example 4: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (82e6d1983b1b49feab1878dd91165223) {'id': '82e6d1983b1b49feab1878dd91165223', 'created_at': datetime.datetime(2024, 3, 30, 18, 3, 8, 670124), 'updated_at': datetime.datetime(2024, 3, 30, 18, 3, 8, 670147)}", "[User] (6614c7076f914f9195914b2b847835ef) {'id': '6614c7076f914f9195914b2b847835ef', 'created_at': datetime.datetime(2024, 3, 30, 18, 3, 39, 438456), 'updated_at': datetime.datetime(2024, 3, 30, 18, 3, 39, 438473), 'first_name': 'David'}"]
```
<br>
