import tkinter as tk
from tkinter import colorchooser

def choose_color1():
    """Abre o seletor de cores para a cor 1 e atualiza a visualização."""
    color = colorchooser.askcolor(title="Escolha a Cor 1")[1]
    if color:
        global color1
        color1 = color
        color1_button.configure(bg=color)
        update_gradient()

def choose_color2():
    """Abre o seletor de cores para a cor 2 e atualiza a visualização."""
    color = colorchooser.askcolor(title="Escolha a Cor 2")[1]
    if color:
        global color2
        color2 = color
        color2_button.configure(bg=color)
        update_gradient()

def update_gradient():
    """Atualiza o fundo do canvas com o gradiente."""
    if color1 and color2:
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        steps = height  # Gradiente vertical em passos igual à altura do canvas
        
        # Limpa o canvas antes de redesenhar
        canvas.delete("gradient")
        
        for i in range(steps):
            ratio = i / steps
            r1, g1, b1 = canvas.winfo_rgb(color1)
            r2, g2, b2 = canvas.winfo_rgb(color2)
            r = int(r1 + (r2 - r1) * ratio) // 256
            g = int(g1 + (g2 - g1) * ratio) // 256
            b = int(b1 + (b2 - b1) * ratio) // 256
            color = f'#{r:02x}{g:02x}{b:02x}'
            canvas.create_rectangle(0, i, width, i + 1, outline=color, fill=color, tags="gradient")

# Janela principal
root = tk.Tk()
root.title("Gradiente de Cores")
root.geometry("600x400")
root.configure(bg="#f0f0f0")

# Variáveis para armazenar as cores
color1 = "#ffffff"  # Cor inicial 1 (branco)
color2 = "#000000"  # Cor inicial 2 (preto)

# Frame superior para botões
frame_top = tk.Frame(root, bg="#f0f0f0")
frame_top.pack(pady=10)

# Botões de seleção de cor
color1_button = tk.Button(frame_top, text="Escolha a Cor 1", bg=color1, command=choose_color1)
color1_button.pack(side=tk.LEFT, padx=10)

color2_button = tk.Button(frame_top, text="Escolha a Cor 2", bg=color2, command=choose_color2)
color2_button.pack(side=tk.LEFT, padx=10)

# Canvas para exibir o gradiente
canvas = tk.Canvas(root, width=600, height=300, bg="#ffffff", highlightthickness=0)
canvas.pack(pady=10, fill=tk.BOTH, expand=True)

# Atualizar gradiente quando a janela for redimensionada
canvas.bind("<Configure>", lambda event: update_gradient())

# Iniciar o loop principal
root.mainloop()
