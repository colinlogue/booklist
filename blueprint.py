from flask import Blueprint, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

from db import RecordsManager, Record

mongo = PyMongo()
booklist = Blueprint('booklist', __name__)

records = RecordsManager()

@booklist.route('/wishlist')
def wishlist():
    items = records.get_wishlist().sort('wishlist_add')
    return render_template('booklist/wishlist.html', items=items)

@booklist.route('/finished')
def finished():
    return "placeholder for finished page"

@booklist.route('/browse')
def browse():
    return "placeholder for browse page"

@booklist.route('/records/<rec_id>')
def view_record(rec_id):
    return f"placeholder for {rec_id} record page"

@booklist.route('/new')
def create_new_record():
    return render_template('booklist/create_record.html')

@booklist.route('/create')
def create_record_action():
    title = request.args.get('title')
    note = request.args.get('note')
    form = 'textual'
    record = records.create_record(title, form)
    record.add_to_wishlist(note)
    return redirect(url_for('.wishlist'))