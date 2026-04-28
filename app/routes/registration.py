from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.event import Event
from ..models.registration import Registration

registration_bp = Blueprint('registration', __name__)

@registration_bp.route('/events/<int:id>/register', methods=['GET'])
def registration_form(id):
    """顯示報名表單"""
    event = Event.get_by_id(id)
    if not event:
        flash("找不到該活動", "danger")
        return redirect(url_for('event.list_events'))
    
    # 檢查是否額滿
    if len(event.registrations) >= event.max_participants:
        flash("該活動已額滿", "warning")
        return redirect(url_for('event.detail', id=id))

    return render_template('registration_form.html', event=event)

@registration_bp.route('/events/<int:id>/register', methods=['POST'])
def register(id):
    """處理報名提交"""
    event = Event.get_by_id(id)
    if not event:
        flash("找不到該活動", "danger")
        return redirect(url_for('event.list_events'))

    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    phone = request.form.get('phone', '').strip()

    # 基本驗證
    if not all([name, email, phone]):
        flash("請填寫所有必填欄位", "danger")
        return redirect(url_for('registration.registration_form', id=id))

    # 檢查名額
    if len(event.registrations) >= event.max_participants:
        flash("很抱歉，名額已滿", "warning")
        return redirect(url_for('event.detail', id=id))

    # 建立報名
    reg_data = {
        'event_id': id,
        'name': name,
        'email': email,
        'phone': phone
    }
    registration = Registration.create(reg_data)
    
    if registration:
        flash("報名成功！", "success")
        return redirect(url_for('registration.success', event_id=id))
    else:
        flash("報名失敗，請稍後再試", "danger")
        return redirect(url_for('registration.registration_form', id=id))

@registration_bp.route('/registration/success')
def success():
    """顯示報名成功頁面"""
    event_id = request.args.get('event_id')
    event = Event.get_by_id(event_id) if event_id else None
    return render_template('registration_success.html', event=event)
