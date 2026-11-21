class Qahramon:
    def __init__(self, ism, jon):
        self.ism = ism
        self.jon = jon

    def malumot(self):
        print(f"Qahramon: {self.ism}")
        print(f"Jon: {self.jon}")

    def hujum(self):
        print("Qahramon hujum qilmoqda.")


class Jangchi(Qahramon):
    def __init__(self, ism, jon, qurol):
        super().__init__(ism, jon)
        self.qurol = qurol

    def malumot(self):
        super().malumot()
        print(f"Qurol: {self.qurol}")

    def hujum(self):
        super().hujum()
        print(f"{self.ism} {self.qurol} bilan hujum qilmoqda.")


jangchi = Jangchi("Knight", 100, "Qilich")

jangchi.malumot()
jangchi.hujum()
