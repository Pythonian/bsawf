from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


debug_toolbar = DebugToolbarExtension()
mail = Mail()
csrf = CSRFProtect()
migrate = Migrate()
db = SQLAlchemy()
login_manager = LoginManager()
