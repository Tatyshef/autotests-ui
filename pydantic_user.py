from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True

invalid_user_data = {
    "id": "ttt",
    "username": "Zara",
    "email": "bond@gmail.com"
}


try:
    invalid_user = User(**invalid_user_data)
except Exception as e:
    print("Ошибка валидации:", e)