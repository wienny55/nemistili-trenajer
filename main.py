import random
import flet as ft

# 100% yopiq va xatosiz lug'at tarkibi
dictionary = {
    "ab": "dan, boshlab",
    "aber": "ammo, lekin, biroq",
    "abfahren": "jo’nab ketmoq",
    "die Abfahrt": "jo’nab ketish",
    "abgeben": "bermoq",
    "abholen": "olib kelmoq",
    "der Absender": "jo‘natuvchi",
    "die Achtung": "diqqat, hurmat",
    "die Adresse": "manzil",
    "all": "hamma, barcha",
    "allein": "yolg’iz, yakka",
    "also": "demak, shunday qilib",
    "alt": "eski, keksa, qari",
    "das Alter": "yosh",
    "an": "ga, da",
    "anbieten": "taklif qilmoq",
    "das Angebot": "taklif",
    "ander": "boshqa",
    "anfangen": "boshlamoq, boshlanmoq",
    "der Anfang": "boshlanish",
    "anklicken": "sichqonchani bosmoq (kompyuter)",
    "ankommen": "yetib kelmoq",
    "die Ankunft": "yetib kelish",
    "ankreuzen": "belgilamoq",
    "anmachen": "yoqmoq (svet…)",
    "anmelden": "ro’yxatdan o‘tmoq, yozilmoq",
    "die Anmeldung": "ro’yxatdan o’tish, qabulxona",
    "die Anrede": "murojaat",
    "anrufen": "qo’ng’iroq qilmoq",
    "der Anruf": "qo’ng‘iroq",
    "antworten": "javob bermoq",
    "die Antwort": "javob",
    "die Anzeige": "e‘lon",
    "anziehen": "kiyinmoq",
    "das Apartment": "kichik kvartira",
    "der Apfel": "olma",
    "der Appetit": "ishtaha",
    "arbeiten": "ishlamoq",
    "die Arbeit": "ish",
    "arbeitslos": "ishsiz",
    "der Arbeitsplatz": "ish joyi, ish o‘rni",
    "der Arm": "qo‘l",
    "der Arzt": "vrach",
    "auch": "ham",
    "auf": "ga, da, ustiga, ustida",
    "die Aufgabe": "vazifa, topshiriq",
    "aufhören": "tugamoq, tamom bo‘lmoq",
    "aufstehen": "o’rnidan turmoq",
    "der Aufzug": "lift",
    "das Auge": "ko‘z",
    "aus": "dan",
    "der Ausflug": "sayr, sayohat",
    "ausfüllen": "to’ldirmoq (anketa)",
    "der Ausgang": "chiqish",
    "die Auskunft": "ma‘lumot",
    "das Ausland": "chet el",
    "der Ausländer": "chet ellik",
    "ausländisch": "xorijiy, chet elga oid",
    "ausmachen": "o’chirmoq (svet)",
    "die Aussage": "fikr",
    "aussehen": "ko‘rinmoq",
    "aussteigen": "tushmoq (transport)",
    "der Ausweis": "hujjat, guvohnoma",
    "ausziehen": "yechinmoq",
    "das Auto": "avtomobil",
    "die Autobahn": "avtomagistral",
    "der Automat": "avtomat",
    "automatisch": "avtomatik",
    "das Baby": "chaqaloq",
    "die Bäckerei": "novvoyxona",
    "das Bad": "vanna, hammom",
    "baden": "cho’milmoq",
    "die Bahn": "yo’l, temiryo‘l",
    "der Bahnhof": "vokzal",
    "der Bahnsteig": "platforma",
    "bald": "yaqinda, tez orada",
    "der Balkon": "balkon",
    "die Banane": "banan",
    "die Bank": "bank, skameyka",
    "bar": "naqd",
    "der Bauch": "qorin",
    "der Baum": "daraxt",
    "der Beamte": "davlat xizmatchisi",
    "bedeuten": "ma’no anglatmoq",
    "beginnen": "boshlanmoq, boshlamoq",
    "bei": "da, huzurida, nikida",
    "beide": "ikkalasi, ikkovi",
    "das Bein": "oyoq",
    "das Beispiel": "misol, namuna",
    "bekannt": "taniqli, mashhur",
    "der Bekannte": "tanish (kishi)",
    "bekommen": "olmoq",
    "benutzten": "foydalanmoq",
    "der Beruf": "kasb",
    "besetzt": "band, egallangan",
    "besichtigen": "borib ko’rmoq, tomosha qilmoq",
    "besser": "yaxshiroq",
    "besten": "eng yaxshi",
    "bestellen": "buyurtma qilmoq",
    "besuchen": "bormoq, qatnamoq, ziyorat qilmoq",
    "das Bett": "to’shak, kravat",
    "bezahlen": "to‘lamoq",
    "das Bier": "pivo",
    "das Bild": "rasm, kartina",
    "billig": "arzon",
    "die Birne": "nok",
    "bis": "gacha",
    "bisschen": "ozgina, kamgina, biroz",
    "bitte": "marhamat, iltimos",
    "bitten": "iltimos qilmoq",
    "bitter": "achchiq, o'tkir",
    "bleiben": "qolmoq",
    "der Bleistift": "qalam",
    "der Blick": "nigoh, nazar",
    "die Blume": "gul",
    "der Bogen": "qog’oz parchasi, varaqa",
    "böse": "jahldor, g'azablangan",
    "brauchen": "kerak bo‘lmoq",
    "breit": "keng",
    "der Brief": "xat, maktub",
    "die Briefmarke": "xat markasi, pochta markasi",
    "bringen": "olib kelmoq, keltirmoq",
    "das Brot": "non",
    "das Brötchen": "bulochka",
    "der Bruder": "aka, uka",
    "das Buch": "kitob",
    "der Buchstabe": "harf",
    "buchstabieren": "harflab aytmoq",
    "der Bus": "avtobus",
    "die Butter": "sariyog‘",
    "das Cafe": "kafe",
    "die CD": "disk",
    "der Chef": "boshliq, rahbar, xo‘jayin",
    "circa": "taxminan",
    "der Computer": "kompyuter",
    "zu": "ga, da",
    "zufrieden": "mamnun, xursand",
    "der Zug": "poezd",
    "zurück": "orqaga",
    "zusammen": "birga, birgalikda",
    "zwischen": "o’rtasida, orasida"
}

class MobileTrenajer:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "TELC B1 Trenajer"
        
        # Yangi versiyada oyna o'lchamlari
        self.page.window = ft.Window(
            width=390,
            height=700,
            resizable=False
        )
        
        # Yangi versiyada alignment matn ("center") ko'rinishida beriladi
        self.page.horizontal_alignment = "center"
        self.page.bgcolor = "#121214"
        
        self.score = 0
        self.words_list = list(dictionary.keys())
        self.correct_ans = ""
        
        # --- UI Elementlari ---
        self.score_text = ft.Text("Ochko: 0 🔥", size=18, weight="bold", color="#FFD700")
        self.german_word = ft.Text("", size=32, weight="bold", color="#FFFFFF", text_align="center")
        
        self.buttons = []
        for i in range(3):
            btn = ft.Button(
                content=ft.Text("", size=16), 
                width=340, 
                height=60,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=12),
                    bgcolor="#1F1F23",
                    color="#E1E1E6"
                ),
                on_click=self.check_answer,
                data=i
            )
            self.buttons.append(btn)
            
        self.status_text = ft.Text("", size=18, weight="500")
        
        self.next_btn = ft.Button(
            content=ft.Text("Keyingi so'z ➡️", color="#3498DB", size=16),
            disabled=True,
            on_click=self.load_question,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
                bgcolor="#1F1F23"
            )
        )
        
        # Elementlarni ekranga joylash (alignment o'rniga "center" matni yozildi)
        self.page.add(
            ft.Container(height=20),
            self.score_text,
            ft.Container(height=40),
            ft.Container(content=self.german_word, alignment="center", width=350, height=100),
            ft.Container(height=20),
            ft.Column(controls=self.buttons, horizontal_alignment="center"),
            ft.Container(height=20),
            self.status_text,
            ft.Container(height=10),
            self.next_btn
        )
        
        self.load_question(None)

    def load_question(self, e):
        self.status_text.value = ""
        self.next_btn.disabled = True
        
        self.current_word = random.choice(self.words_list)
        self.correct_ans = dictionary[self.current_word]
        
        wrong_pool = [v for k, v in dictionary.items() if v != self.correct_ans]
        options = [self.correct_ans] + random.sample(wrong_pool, 2)
        random.shuffle(options)
        
        self.german_word.value = self.current_word
        for i in range(3):
            self.buttons[i].content.value = options[i]
            self.buttons[i].style.bgcolor = "#1F1F23"
            self.buttons[i].disabled = False
            
        self.page.update()

    def check_answer(self, e):
        clicked_btn = e.control
        
        for btn in self.buttons:
            btn.disabled = True
            if btn.content.value == self.correct_ans:
                btn.style.bgcolor = "#2ECC71"  # To'g'ri javob yashil bo'ladi
                
        if clicked_btn.content.value == self.correct_ans:
            self.score += 1
            self.score_text.value = f"Ochko: {self.score} 🔥"
            self.status_text.value = "Barakalla! To'g'ri 🎉"
            self.status_text.color = "#2ECC71"
        else:
            clicked_btn.style.bgcolor = "#E74C3C"  # Xato bosilgan tugma qizil bo'ladi
            self.status_text.value = "Xato! Keyingisida omad keladi 🧐"
            self.status_text.color = "#E74C3C"
            
        self.next_btn.disabled = False
        self.page.update()

if __name__ == "__main__":
    ft.run(MobileTrenajer)