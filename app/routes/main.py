from flask import Blueprint, render_template, request
from ..models.event import Event

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """顯示首頁，列出即將到來的活動"""
    events = Event.get_all()
    # 限制首頁只顯示前 6 筆
    featured_events = events[:6]
    return render_template('index.html', events=featured_events)

@main_bp.route('/search')
def search():
    """搜尋活動"""
    query = request.args.get('q', '').strip()
    if not query:
        return render_template('search_results.html', events=[], query=query)
    
    # 簡單的標題模糊搜尋
    all_events = Event.get_all()
    results = [e for e in all_events if query.lower() in e.title.lower() or query.lower() in e.description.lower()]
    
    return render_template('search_results.html', events=results, query=query)
