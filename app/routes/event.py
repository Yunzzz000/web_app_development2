from flask import Blueprint, render_template, abort

event_bp = Blueprint('event', __name__, url_prefix='/events')

@event_bp.route('/')
def list_events():
    """顯示活動列表"""
    pass

@event_bp.route('/<int:id>')
def detail(id):
    """顯示活動詳情"""
    pass
