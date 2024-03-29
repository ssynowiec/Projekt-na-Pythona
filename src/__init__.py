# Initialization file for all contents of 'src' directory.
# The content of the file is extremely important globally for the entire application. So do not remove
# anything from it that could in any way affect the functioning of the application.
#
# <Flask's main data package>
from flask import Flask
from flask_cors import CORS

from src.utils.EnvSystem import EnvSystem
from src.utils.FileSystem import FileSystem

app: Flask = Flask(__name__,
                   root_path=str(FileSystem.get_root_folder()),
                   template_folder='templates',
                   static_folder='public')

CORS(app)

###########################################################################
# Server log system.
from src.utils.LogSystem import LogSystem

log: LogSystem = LogSystem()

###########################################################################
# All files in the <view> directory should go here.
# Thanks to this, we clearly tell flask that such files are somewhere in the project and we give it
# information that they are used to render the image of the web application.
import src.view.ControllerView
import src.api
