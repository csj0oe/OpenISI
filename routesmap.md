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