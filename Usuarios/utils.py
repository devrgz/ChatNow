
   
def get_user_image(self, filename):
    return f"avatar/{str(self.pk)}/{'perfil_image.png'}"

def get_default_image(self, filename):
        return f"avatar/'perfil_image_default.jpg'"
