from datetime import datetime
import pytz


timezone = pytz.timezone("America/Los_Angeles")
def local_now():
    return timezone.localize(datetime.now())


FORMS = [
    'textual', # could be a printed book or audiobook
    'audiovisual', # movies, TV shows, etc.
    'musical' # albums, compositions
]


class RecordsManager:

    def __init__(self):
        self.collection = None

    def create_record(self, title, form, info=None):
        if not info:
            info = {}
        assert title
        assert form in FORMS
        info['title'] = title
        info['form'] = form
        rec_id = self.collection.insert_one(info).inserted_id
        return Record(title, form, info, self.collection, rec_id)

    def get_wishlist(self):
        return self.collection.find({'on_wishlist': True})

    def init_mongo(self, mongo):
        self.collection = mongo.db.booklist



class Record:

    def __init__(self, title, form, info, collection, rec_id):
        self.title = title
        self.form = form
        self.info = info
        if not "notes" in self.info:
            self.info["notes"] = []
        if not "on_wishlist" in self.info:
            self.info["on_wishlist"] = False
        if not "finished" in self.info:
            self.info["finished"] = False
        if not "tags" in self.info:
            self.info["tags"] = []
        self.collection = collection
        self.rec_id = rec_id

    def add_note(self, text):
        note = {'text': text, 'created': local_now()}
        update = {'$addToSet': {'notes': note}}
        self.collection.update_one({'_id': self.rec_id}, update)

    def add_tags(self, tags_list):
        tags_field = self.info["tags"]
        for tag in tags_list:
            if not tag in tags_field:
                tags_field.append(tag)
        self.update({'tags': tags_field})

    def add_to_wishlist(self, note=None):
        wishlist_fields = {'on_wishlist': True}
        if not self.info['on_wishlist']:
            wishlist_fields['wishlist_add'] = local_now()
        if note:
            wishlist_fields['wishlist_note'] = note
        self.update(wishlist_fields)

    def mark_finished(self):
        self.update({'on_wishlist': False})
        self.update({'finished': True})

    def remove_tags(self, tags_list):
        tags_field = self.info["tags"]
        for tag in tags_list:
            if tag in tags_field:
                tags_field.remove(tag)
        self.update({'tags': tags_field})

    def update(self, fields):
        self.collection.update_one({'_id': self.rec_id}, {'$set': fields})
        for key in fields:
            self.info[key] = fields[key]