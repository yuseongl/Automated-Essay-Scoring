class HistoryRepository:
    def __init__(self, db):
        self.db = db

def save(self, user_id: str, event_type: str, payload: dict):
        history_entry = {
            "user_id": user_id,
            "event_type": event_type,
            "payload": payload
        }
        self.db.history.insert_one(history_entry)

def load(self, user_id: str, event_type: str):
        return list(self.db.history.find({"user_id": user_id, "event_type": event_type})) 



'''
    def add_history(self, user_id, essay_id, feedback):
        history_entry = {
            "user_id": user_id,
            "essay_id": essay_id,
            "feedback": feedback
        }
        self.db.history.insert_one(history_entry)

    def get_history(self, user_id):
        return list(self.db.history.find({"user_id": user_id}))

    def clear_history(self, user_id):
        self.db.history.delete_many({"user_id": user_id})
        '''