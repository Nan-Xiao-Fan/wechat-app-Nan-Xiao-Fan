from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pymysql


app = FastAPI()

# 添加跨域支持
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/swiper")
def get_swiper_data():
    swiper_data = [
        {"imgurl": "C:/Users/xp/Desktop/banner/banner1.jpg"},
        {"imgurl": "C:/Users/xp/Desktop/banner/banner2.jpg"},
    ]
    return swiper_data




# 数据库连接配置
db_config = {
    "host": "localhost",
    "user": "your_username",
    "password": "your_password",
    "database": "your_database_name",
}


class UserCreateRequest(BaseModel):
    username: str
    address: str
    phone: str


class UserUpdateRequest(BaseModel):
    address: str
    phone: str


class UserCreateRequest(BaseModel):
    username: str
    address: str
    phone: str


class UserUpdateRequest(BaseModel):
    address: str
    phone: str


@app.post("/users")
def create_user(user: UserCreateRequest):
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()

    # 将用户信息插入数据库
    insert_query = "INSERT INTO users (username, address, phone) VALUES (%s, %s, %s)"
    values = (user.username, user.address, user.phone)
    cursor.execute(insert_query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "User created successfully"}


@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdateRequest):
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()

    # 更新用户信息
    update_query = "UPDATE users SET address = %s, phone = %s WHERE id = %s"
    values = (user.address, user.phone, user_id)
    cursor.execute(update_query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "User updated successfully"}


@app.post("/users")
def create_user(user: UserCreateRequest):
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()

    # 将用户信息插入数据库
    insert_query = "INSERT INTO users (username, address, phone) VALUES (%s, %s, %s)"
    values = (user.username, user.address, user.phone)
    cursor.execute(insert_query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "User created successfully"}


@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdateRequest):
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()

    # 更新用户信息
    update_query = "UPDATE users SET address = %s, phone = %s WHERE id = %s"
    values = (user.address, user.phone, user_id)
    cursor.execute(update_query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "User updated successfully"}
