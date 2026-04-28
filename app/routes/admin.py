from flask import Blueprint, render_template, request, redirect, url_for

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/events')
def manage_events():
    """管理活動列表"""
    pass

@admin_bp.route('/events/new', methods=['GET', 'POST'])
def create_event():
    """建立新活動"""
    pass

@admin_bp.route('/events/<int:id>/edit', methods=['GET'])
def edit_event_page(id):
    """編輯活動頁面"""
    pass

@admin_bp.route('/events/<int:id>/update', methods=['POST'])
def update_event(id):
    """更新活動"""
    pass

@admin_bp.route('/events/<int:id>/delete', methods=['POST'])
def delete_event(id):
    """刪除活動"""
    pass
