import customtkinter as ctk
from PIL import Image


class ImageButton(ctk.CTkButton):
    def __init__(
        self,
        master,
        image_path: str,
        width: int = 120,
        height: int = 40,
        image_width: int = 24,
        image_height: int = 24,
        text: str = "",
        font=("Arial", 14),
        fg_color="#840909",
        hover_color="#9a1f21",
        hover=True,
        text_color="white",
        command=None,
        **kwargs
    ):
        self.image = ctk.CTkImage(
            light_image=Image.open(image_path),
            dark_image=Image.open(image_path),
            size=(image_width, image_height)
        )

        super().__init__(
            master=master,
            width=width,
            height=height,
            text=text,
            image=self.image,
            font=font,
            fg_color=fg_color,
            hover_color=hover_color,
            hover=hover,
            text_color=text_color,
            command=command,
            **kwargs
        )