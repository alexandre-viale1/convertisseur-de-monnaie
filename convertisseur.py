import tkinter as tk
from tkinter import *
#définition de toute les fonctions du programme
def convertion():
    montant = float(montant_a_convertir.get())
    de_la_devise = var1.get()
    vers_la_devise = var2.get()
    taux = rate[de_la_devise]/rate[vers_la_devise]
    resultat = round(montant * taux, 2)
    resultat_convertion.delete(0, tk.END)
    resultat_convertion.insert(0, resultat)
    history.append(f"{montant} {vers_la_devise} = {resultat} {de_la_devise}")
    historique.insert(tk.END, history[-1])
#creation de la fenetre
fenetre = tk.Tk()
fenetre.title("Convertisseur")
fenetre.geometry("250x250")
#incrementation de taux de change par rapport a l'euro
rate = {"Euro:€": 1, "Dollar:$": 1.09, "Yen:¥": 141.70, "Livre:£": 0.88, "Roupie indienne:₹": 88.84}
#creation des boutons
var1 = tk.StringVar(value="...")
var2 = tk.StringVar(value="...")

montant1 = Label(fenetre , text="De")
montant1.grid(row=1, column=0)
monnaie1 = tk.OptionMenu(fenetre, var1, *rate)
monnaie1.grid(row=2, column=1)

monnaie2 = tk.OptionMenu(fenetre, var2, *rate)
monnaie2.grid(row=1, column=1)
montant2 = Label(fenetre , text="Vers")
montant2.grid(row=2, column=0)

montant_a_convertir = tk.Entry(fenetre)
montant_a_convertir.grid(row=0, column=1)
montant = Label(fenetre, text="Montant : ")
montant.grid(row=0 , column=0)

resultat = Label(fenetre, text="Résultat : ")
resultat.grid(row=4 , column=0)
resultat_convertion = tk.Entry(fenetre)
resultat_convertion.grid(row=4, column=1)

convertion = tk.Button(fenetre, text="Convertir", command=convertion,height=2, width=10, background="#63ABFC")
convertion.grid(row=3, column=0)

history = []
historique = tk.Listbox(fenetre, width=40)
historique.grid(row=5, column=0, padx=5, pady=5, columnspan=2, )

fenetre.mainloop()