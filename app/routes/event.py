from flask import Blueprint, render_template, abort
from ..models.event import Event

event_bp = Blueprint('event', __name__, url_prefix='/events')

@event_bp.route('/')
def list_events():
    """顯示活動列表"""
    events = Event.get_all()
    return render_template('event_list.html', events=events)

@event_bp.route('/<int:id>')
def detail(id):
    """顯示活動詳情"""
    event = Event.get_by_id(id)
    if not event:
        abort(404)
    return render_template('event_detail.html', event=event)
