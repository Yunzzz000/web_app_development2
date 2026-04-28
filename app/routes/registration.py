from flask import Blueprint, render_template, request, redirect, url_for

registration_bp = Blueprint('registration', __name__)

@registration_bp.route('/events/<int:id>/register', methods=['GET'])
def registration_form(id):
    """顯示報名表單"""
    pass

@registration_bp.route('/events/<int:id>/register', methods=['POST'])
def register(id):
    """處理報名提交"""
    pass

@registration_bp.route('/registration/success')
def success():
    """顯示報名成功頁面"""
    pass
