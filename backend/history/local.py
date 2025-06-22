import json, os

class LocalHistoryRepository:
    def __init__(self, file_path='history_logs'):
        os.makedirs(file_path, exist_ok=True)
        self.file_path = file_path
        
    def save(self, user_id: str, event_type: str, payload: dict):
        file_name = f"{self.file_path}/{user_id}_{event_type}.json"
        data = self.load(user_id, event_type)
        data.append(payload)
        with open(file_name, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            
    def load(self, user_id: str, event_type: str):
        file_name = f"{self.file_path}/{user_id}_{event_type}.json"
        if not os.path.exists(file_name):
            return []
        with open(file_name, 'r') as f:
            return json.load(f)
    
    def clear(self, user_id: str, event_type: str):
        file_name = f"{self.file_path}/{user_id}_{event_type}.json"
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print(f"No history found for user {user_id} with event type {event_type}.")