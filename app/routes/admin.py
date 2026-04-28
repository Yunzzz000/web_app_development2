from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.event import Event
from datetime import datetime

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/events')
def manage_events():
    """管理活動列表"""
    events = Event.get_all()
    return render_template('admin/event_list.html', events=events)

@admin_bp.route('/events/new', methods=['GET', 'POST'])
def create_event():
    """建立新活動"""
    if request.method == 'POST':
        data = {
            'title': request.form.get('title'),
            'description': request.form.get('description'),
            'category': request.form.get('category'),
            'location': request.form.get('location'),
            'event_date': datetime.strptime(request.form.get('event_date'), '%Y-%m-%dT%H:%M'),
            'registration_deadline': datetime.strptime(request.form.get('registration_deadline'), '%Y-%m-%dT%H:%M'),
            'max_participants': int(request.form.get('max_participants', 0)),
            'image_url': request.form.get('image_url')
        }
        
        # 基本驗證
        if not all([data['title'], data['description'], data['event_date']]):
            flash("請填寫必填欄位", "danger")
            return render_template('admin/event_form.html', action="新增", event=None)
            
        event = Event.create(data)
        if event:
            flash("活動建立成功！", "success")
            return redirect(url_for('admin.manage_events'))
        else:
            flash("建立失敗", "danger")

    return render_template('admin/event_form.html', action="新增", event=None)

@admin_bp.route('/events/<int:id>/edit', methods=['GET'])
def edit_event_page(id):
    """編輯活動頁面"""
    event = Event.get_by_id(id)
    if not event:
        flash("活動不存在", "danger")
        return redirect(url_for('admin.manage_events'))
    return render_template('admin/event_form.html', event=event, action="編輯")

@admin_bp.route('/events/<int:id>/update', methods=['POST'])
def update_event(id):
    """更新活動"""
    event = Event.get_by_id(id)
    if not event:
        flash("活動不存在", "danger")
        return redirect(url_for('admin.manage_events'))
        
    data = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'category': request.form.get('category'),
        'location': request.form.get('location'),
        'event_date': datetime.strptime(request.form.get('event_date'), '%Y-%m-%dT%H:%M'),
        'registration_deadline': datetime.strptime(request.form.get('registration_deadline'), '%Y-%m-%dT%H:%M'),
        'max_participants': int(request.form.get('max_participants', 0)),
        'image_url': request.form.get('image_url')
    }
    
    if event.update(data):
        flash("活動更新成功！", "success")
    else:
        flash("更新失敗", "danger")
        
    return redirect(url_for('admin.manage_events'))

@admin_bp.route('/events/<int:id>/delete', methods=['POST'])
def delete_event(id):
    """刪除活動"""
    event = Event.get_by_id(id)
    if event and event.delete():
        flash("活動已刪除", "success")
    else:
        flash("刪除失敗", "danger")
    return redirect(url_for('admin.manage_events'))
