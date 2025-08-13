from earth import Human 🌍

class ItMe(Human):
    first_name = "Hassan"  # ✨
    last_name = "Sayed"    # 🚀
    work_where = "SBS"     # 🏢
    work_what = "Software Engineer"  # 💻

    @classmethod
    def hi(cls):
        print(f"Hey 👋, I'm {cls.first_name} {cls.last_name} 😄")
        print(f"💼 Currently I work as a {cls.work_what} @ {cls.work_where} 🏆")

ItMe.hi()


### 👨‍💻 About Me
- 🏢 **Software Engineer** @ SBS
- 🌱 Passionate about APIs, backend systems, and clean code
- ⚡ Fun fact: I turn ☕ into code
