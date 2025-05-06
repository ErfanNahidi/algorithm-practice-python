import json

# مسیر فایل نوت‌بوک معیوب
file_path = '/home/crow/Documents/CS_File/Trains/algo/1.ipynb'

# تلاش برای خواندن فایل و اصلاح ساختار
try:
    with open(file_path, 'r') as f:
        content = f.read()

    # بررسی محتوای فایل که به درستی بارگذاری نشده است
    if not content:
        print("فایل خالی است یا خراب شده.")
    else:
        print("محتوا خوانده شد. تلاش برای اصلاح فایل.")
        # سعی می‌کنیم که ابتدا فایل را اصلاح کنیم
        try:
            notebook = json.loads(content)  # سعی می‌کنیم داده‌ها را تجزیه کنیم

            # بررسی ساختار نوت‌بوک
            if 'cells' not in notebook:
                raise ValueError("ساختار نوت‌بوک مشکل دارد!")

            # ذخیره نوت‌بوک اصلاح شده
            with open(file_path, 'w') as f:
                json.dump(notebook, f, indent=2)  # ذخیره به فرمت صحیح JSON

            print("فایل نوت‌بوک با موفقیت اصلاح شد.")
        except json.JSONDecodeError:
            print("خطای JSON موجود در فایل. محتوا ممکن است خراب شده باشد.")
except FileNotFoundError:
    print("فایل مورد نظر پیدا نشد.")
except Exception as e:
    print(f"خطای غیرمنتظره: {e}")
