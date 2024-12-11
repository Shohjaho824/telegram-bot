START = \
"""
Assalomu alaykum 👋🏻
"""
NAME = \
"""
Ismingizni kiriting❗️
""" 
AGE_HANDLER = \
"""
Yoshingizni kiriting❗️
""" 
PHONE_HANDLER = \
"""
ILTIMOS telefon raqamingizni yozib yuboring yoki pasatdagi telefon raqam yuborish tugmasini bosing
"""
KURSLAR = \
"""
Qaysi kursni tanlamoqchisiz!
""" 

def check(**kwargs):
    application = ''

    application += f"MA'LUMOT:\n"
    application += f"Ism :{kwargs['name']}\n"
    application += f"Yosh :{kwargs['age']}\n"
    application += f"Telefon :{kwargs['pxone']}\n"
    application += f"Kurslar :{kwargs['fields']}\n"

    return application
