import web

urls = ('/upload', 'Upload')

class Upload:
    def GET(self):
        return """<html><head></head><body>
                    <form method="POST" enctype="multipart/form-data" action="">
                    <input type="file" name="myfile" />
                    <br/>
                    <input type="submit" />
                    </form>
                    </body></html>"""

    def POST(self):
        x = web.input(myfile={})
        #web.debug(x['myfile'].filename) # This is the filename
        #web.debug(x['myfile'].value) # This is the file contents

        # writes the file to the same filename in the current directory
        # modify this to output to some other directory if you wish
        target = open(x['myfile'].filename, 'w')
        target.write(x['myfile'].value)
        target.close()

        raise web.seeother('/upload')

if __name__ == "__main__":
    app = web.application(urls, globals()) 
    app.run()
