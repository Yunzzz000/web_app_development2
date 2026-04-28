from flask import Blueprint, render_template, request

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """顯示首頁"""
    pass

@main_bp.route('/search')
def search():
    """搜尋活動"""
    pass
