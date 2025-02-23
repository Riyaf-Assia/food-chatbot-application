import re
def extract_session_id(session:str):
    match = re.search(r'\/sessions\/(.*?)\/contexts',session)
    if match:
        return match.group(1)
    return ""

def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result

if __name__ == "__main__":
    print(get_str_from_food_dict({"pizza":5,"sambosa":4}))