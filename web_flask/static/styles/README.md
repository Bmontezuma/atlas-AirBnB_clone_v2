# ***Write a script that starts a Flask web application:***

- Your web application must be listening on ***0.0.0.0***, port ***5000***
- You must use ***storage*** for fetching data from the storage engine (***[FileStorage](https://github.com/Bmontezuma/atlas-AirBnB_clone_v2/blob/main/models/engine/file_storage.py)*** or ***[DBStorage](https://github.com/Bmontezuma/atlas-AirBnB_clone_v2/blob/main/models/engine/db_storage.py)***) => ***from models import storage*** and ***storage.all***(...)
- To load all cities of a ***State***:
    - If your storage engine is ***[DBStorage](https://github.com/Bmontezuma/atlas-AirBnB_clone_v2/blob/main/models/engine/db_storage.py)***, you must use ***cities*** relationship
    - Otherwise, use the public getter method ***cities***
- After each request you must remove the current SQLAlchemy Session:
    - Declare a method to handle ***@app.teardown_appcontext***
    - Call in this method ***storage.close()***
- Routes:
    - ***/hbnb_filters***: display a HTML page like ***[6-index.html](https://github.com/Bmontezuma/atlas-AirBnB_clone_v2/blob/main/web_static/6-index.html)***, which was done during the project ***[0x01. AirBnB clone - Web static](https://github.com/Bmontezuma/atlas-AirBnB_clone_v2/tree/main/web_static)***
    - Copy files ***[3-footer.css](https://github.com/Bmontezuma/atlas-AirBnB_clone_v2/blob/main/web_static/styles/3-footer.css)***, ***[3-header.css](https://github.com/Bmontezuma/atlas-AirBnB_clone_v2/blob/main/web_static/styles/3-header.css)***, ***[4-common.css](https://github.com/Bmontezuma/atlas-AirBnB_clone_v2/blob/main/web_static/styles/4-common.css)*** and ***[6-filters.css](https://github.com/Bmontezuma/atlas-AirBnB_clone_v2/blob/main/web_static/styles/6-filters.css)*** from ***[web_static/styles/](https://github.com/Bmontezuma/atlas-AirBnB_clone_v2/tree/main/web_static/styles)*** to the folder ***[web_flask/static/styles](https://github.com/Bmontezuma/atlas-AirBnB_clone_v2/tree/main/web_flask/static/styles)***
    - Copy files ***icon.png*** and ***[logo.png](https://github.com/Bmontezuma/atlas-AirBnB_clone_v2/blob/main/web_static/images/logo.png)*** from ***[web_static/images/](https://github.com/Bmontezuma/atlas-AirBnB_clone_v2/tree/main/web_static/images)*** to the folder ***[web_flask/static/images]()***
    - Update ***.popover*** class in ***6-filters.css*** to allow scrolling in the popover and a max height of 300 pixels.
    - Use ***6-index.html*** content as source code for the template ***10-hbnb_filters.html:***
        - Replace the content of the ***H4*** tag under each filter title (***H3*** States and ***H3*** Amenities) by ***&nbsp***;
- ***State***, ***City*** and ***Amenity*** objects must be loaded from ***DBStorage*** and ***sorted by name*** (A->Z)
- You must use the option ***strict_slashes=False*** in your route definition
- Import this ***10-dump*** to have some data

## ***IMPORTANT***

= Make sure you have a running and valid ***setup_mysql_dev.sql*** in your ***AirBnB_clone_v2*** repository (***Task***)
- Make sure all tables are created when you run ***echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py***

```
guillaume@ubuntu:~/AirBnB_v2$ curl -o 10-dump.sql "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 10-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.10-hbnb_filters
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
## ***In the browser:***

   

Repo:

- GitHub repository: ***atlas-AirBnB_clone_v2***
- File: ***web_flask/10-hbnb_filters.py, web_flask/templates/10-hbnb_filters.html, web_flask/static/***
