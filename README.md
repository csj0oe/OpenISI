# OpenISI

## About
Small private university website on OpenShift platform using Python and MongoDB.

## How to use
### Linux
```shell
python3 wsgi.py
```
### Windows
```shell
1) python : https://www.python.org/ftp/python/3.5.1/python-3.5.1.exe
2) run cmd : pip install bottle
3) double click on : wsgi.py
4) open : http://localhost:8080/
```

## Site Map
```shell
Site/:
	app/:
		# API files + server [Tarek+Amine]
		main.py
	web/
		# Web interface files [Zeus]
		index.html
	ftp/
		# Shared files
		# ModuleName-Class-Year
```

## Routes
```shell
# ROUTE             : File::Function()      # Description

/                   : web::site_web()       # main page - usage info - api doc - .....
/{FILE}             : web::site_web()
/web                : web::site_web()
/web/               : web::site_web()
/web/{FILE}         : web::site_web()

/ftp/{FILE}         : ftp::site_ftp()

/file               : file::list()          # list of all files categorized
/file/{ID}          : file::info()          # file information
/file/search/...    : file::search(...)     # search for file
```