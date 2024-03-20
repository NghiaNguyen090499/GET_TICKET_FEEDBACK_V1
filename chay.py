import subprocess

def run_django_server():
    try:
        # Chạy lệnh python manage.py runserver
        subprocess.run(["python", "manage.py", "runserver"])
    except KeyboardInterrupt:
        # Ngắt chương trình nếu người dùng nhấn Ctrl+C
        print("Server đã dừng.")

if __name__ == "__main__":
    run_django_server()
