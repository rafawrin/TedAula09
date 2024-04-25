import customtkinter as tk
#configurar aparencia
tk.set_appearance_mode('dark')
tk.set_default_color_theme('dark-blue')
#Configurar Janela
app = tk.CTk()
app.geometry('400x240')
app.title('Contador de Vogais')

def conta_vogais():
    palavra = palavra_entry.get()
    vogais = 'aeiouAEIOU'
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    resultado.configure(text=f'Essa palavra tem {contador} vogais!')
mensagem = tk.CTkLabel(app, text='Digite uma palavra')
mensagem.pack(pady = 20)

palavra_entry = tk.CTkEntry(app)
palavra_entry.pack(pady = 10)

resultado = tk.CTkLabel(app, text="")
resultado.pack()

botao = tk.CTkButton(app, text="Contar Vogais", command=conta_vogais)
botao.pack()


#iniciar janela
app.mainloop()