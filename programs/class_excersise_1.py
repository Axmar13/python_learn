class MobilePhone:
    status = 0
    app = None

    def __init__(self, manufacturer=None, screen_size=None, num_cores=None) -> None:
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        
    def power_on(self):
        if self.status == 0:
            self.status = 1
            print("Celular encendido.")
        else:
            print("El celular ya se encuentra prendido.")

    def power_off(self):
        if self.status == 1:
            self.status = 0
            print("Celular apagado.")
        else:
            print("El celular ya se encuentra apagado.")

    def install_app(self, app):
        if self.app != app:            
            self.app = app
            print(f"{self.app} instalada correctamente.")
        else:
            print("La app ya se encuentra instalada.")

    def uninstall_app(self, app):
        if self.app == app:
            print(f"{self.app} desinstalada correctamente")
            self.app = None
        else:
            print("La app no se encuentra instalada.")

phone = MobilePhone("Xiaomi", 6.43, 8)
print(f"Manufacturer: {phone.manufacturer}; Screen Size: {phone.screen_size}; Cores Num: {phone.num_cores}")
phone.power_on()
phone.power_on()
phone.power_off()
phone.power_off()
phone.install_app(None)
phone.install_app("Google")
phone.uninstall_app("Google+")
phone.uninstall_app("Google")
phone.install_app(None)

