# Yemen-Tool-V6 - أداة اليمن لحماية الابتزاز
# Developed by Abdulwahab-Dhamar 🇾🇪
# أداة توعية وحماية - ضد الابتزاز الإلكتروني

import os
print("🇾🇪 اليمن - Yemen-Tool-V6")
print("="*40)
print("مرحبا بك يا عبدالوهاب من ذمار ❤️")
print("أداة الحماية من الابتزاز")
print("="*40)

def check_link():
    link = input("\n🔗 الصق رابط مشبوه لفحصه: ")
    bad_words = ["bit.ly", "tinyurl", "free-money", "hack", "verify-account"]
    for word in bad_words:
        if word in link:
            print("⚠️ تحذير: هذا الرابط مشبوه جداً! لا تفتحه!")
            return
    print("✅ الرابط يبدو سليم لكن انتبه دائماً!")

def tips():
    print("\n📚 نصائح ذهبية ضد الابتزاز:")
    print("1 - لا ترسل صور خاصة لأي شخص")
    print("2 - فعل التحقق بخطوتين في كل حساباتك")
    print("3 - لا تفتح روابط من أشخاص لا تعرفهم")
    print("4 - اذا تم ابتزازك، لا تدفع! بلغ فوراً")
    print("5 - احتفظ بكل الأدلة والمحادثات")

while True:
    print("\n--- القائمة ---")
    print("1 - فحص رابط مشبوه")
    print("2 - نصائح الحماية")
    print("3 - خروج")
    choice = input("اختر رقم: ")
    if choice == "1":
        check_link()
    elif choice == "2":
        tips()
    elif choice == "3":
        print("تحيا اليمن! 🇾🇪 مع السلامة يا بطل ذمار!")
        break
