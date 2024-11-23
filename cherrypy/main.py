import subprocess
import cherrypy
import shlex
# Get the list of all files and directories



class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Site Under Construction<br/>use /generate?cmd=&lt;YOUR COMMAND&gt;<br/>to execute command to configure the server as ssh is not installed.<br /> <br />"

    @cherrypy.expose
    def generate(self,cmd):
        proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
        output = proc.stdout.read()
        return output

cherrypy.server.socket_host = '0.0.0.0'
cherrypy.quickstart(HelloWorld())
