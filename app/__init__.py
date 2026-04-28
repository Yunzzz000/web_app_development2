import os
from flask import Flask
from .models.event import db

def create_app(test_config=None):
    # 建立與設定 Flask app
    app = Flask(__name__, instance_relative_config=True)
    
    # 預設設定
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(app.instance_path, 'database.db'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is None:
        # 如果有 config.py，從中載入設定
        app.config.from_pyfile('config.py', silent=True)
    else:
        # 載入測試設定
        app.config.from_mapping(test_config)

    # 確保 instance 資料夾存在
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 初始化資料庫
    db.init_app(app)

    # 註冊 Blueprints
    from .routes.main import main_bp
    from .routes.event import event_bp
    from .routes.registration import registration_bp
    from .routes.admin import admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(event_bp)
    app.register_blueprint(registration_bp)
    app.register_blueprint(admin_bp)

    # 建立資料庫表格的 CLI 指令
    @app.cli.command("init-db")
    def init_db():
        """清除現有資料並建立新表格"""
        db.create_all()
        print("Initialized the database.")

    # 讓 templates 可以使用 datetime.now()
    @app.context_processor
    def inject_now():
        from datetime import datetime
        return {'now': datetime.utcnow()}

    return app
