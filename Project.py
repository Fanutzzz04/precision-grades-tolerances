import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

##############################--- DATELE DIN TABELUL 3.7 ---

tabel_it = {
    'IT01': (0.6, 0.6), 'IT0': (1, 1), 'IT1': (1.5, 1.5),
    'IT2': (2.5, 2.5),  'IT3': (4, 4), 'IT4': (6, 7),
    'IT5': (9, 11),     'IT6': (13, 16), 'IT7': (21, 25),
    'IT8': (33, 39),    'IT9': (52, 62), 'IT10': (84, 100),
    'IT11': (130, 160),
    'IT12': (0.21, 0.25), 'IT13': (0.33, 0.39), 'IT14': (0.52, 0.62),
    'IT15': (0.84, 1.0),  'IT16': (1.3, 1.6),   'IT17': (2.1, 2.5),
    'IT18': (3.3, 3.9)
}

def identifica():
    try:
        
        try:
            N = float(entry_dim.get())
            Es = float(entry_sup.get()) 
            Ei = float(entry_inf.get()) 
        except ValueError:
            messagebox.showwarning("Eroare", "Introdu doar numere valide!")
            return


        if N < 20 or N > 50:
            messagebox.showerror("Eroare", "Dimensiunea trebuie să fie între 20 și 50 mm.")
            return

       
    
        T_calc_mm = abs(Es - Ei)
        
        
        T_calc_mm = round(T_calc_mm, 4)

    
        idx = 0
        if 18 < N <= 30:
            idx = 0
        elif 30 < N <= 50:
            idx = 1
        

        treapta_gasita = None
        valoare_din_tabel = 0
        
        
        for treapta, valori in tabel_it.items():
            val_tabel_raw = valori[idx]
            
         
            if treapta in ['IT12','IT13','IT14','IT15','IT16','IT17','IT18']:
                val_tabel_mm = val_tabel_raw
            else:
                val_tabel_mm = val_tabel_raw / 1000.0 
            
           
            if abs(T_calc_mm - val_tabel_mm) < 0.00001:
                treapta_gasita = treapta
                valoare_din_tabel = val_tabel_mm
                break

     
        lbl_rez_tol.config(text=f"{T_calc_mm:.4f} mm")
        
        if treapta_gasita:
           
            lbl_rez_it.config(text=f"{treapta_gasita}", fg="green")
            msg = f"Valoarea calculată ({T_calc_mm} mm) corespunde standardului {treapta_gasita}."
            lbl_info.config(text=msg, fg="black")
        else:
         
            lbl_rez_it.config(text="NECUNOSCUTĂ", fg="red")
            lbl_info.config(text="Toleranța calculată nu se regăsește în Tabelul 3.7.", fg="red")

    except Exception as e:
        messagebox.showerror("Eroare", f"A aparut o problema: {e}")

###################### --- INTERFAȚA GRAFICĂ ---
app = tk.Tk()
app.title("Identificare Treaptă Precizie")
app.geometry("400x550")

tk.Label(app, text="Detector Treaptă de Precizie", font=("Arial", 14, "bold"), pady=15).pack()

frame_in = tk.Frame(app, padx=20)
frame_in.pack(fill="x")

# Inputs
tk.Label(frame_in, text="1. Dimensiune Nominală (mm):", font=("Arial", 10)).pack(anchor="w")
entry_dim = tk.Entry(frame_in)
entry_dim.pack(fill="x", pady=5)

tk.Label(frame_in, text="2. Abaterea Superioară (mm):", font=("Arial", 10)).pack(anchor="w")
entry_sup = tk.Entry(frame_in)
entry_sup.pack(fill="x", pady=5)
tk.Label(frame_in, text="(ex: 0.025 sau -0.010)", font=("Arial", 8), fg="gray").pack(anchor="e")

tk.Label(frame_in, text="3. Abaterea Inferioară (mm):", font=("Arial", 10)).pack(anchor="w")
entry_inf = tk.Entry(frame_in)
entry_inf.pack(fill="x", pady=5)
tk.Label(frame_in, text="(ex: 0 sau -0.035)", font=("Arial", 8), fg="gray").pack(anchor="e")

# Buton
btn = tk.Button(app, text="IDENTIFICĂ TREAPTA", bg="#FF5722", fg="white", font=("Arial", 11, "bold"), command=identifica)
btn.pack(pady=20, ipadx=20)

# Rezultate
ttk.Separator(app).pack(fill='x', padx=20)
frame_out = tk.Frame(app, padx=20, pady=10)
frame_out.pack(fill="x")

tk.Label(frame_out, text="Toleranța Calculată (Es - Ei):", font=("Arial", 10)).pack()
lbl_rez_tol = tk.Label(frame_out, text="-", font=("Arial", 12, "bold"))
lbl_rez_tol.pack()

tk.Label(frame_out, text="Treapta de Precizie Identificată:", font=("Arial", 10)).pack(pady=(15,0))
lbl_rez_it = tk.Label(frame_out, text="-", font=("Arial", 18, "bold"), fg="blue")
lbl_rez_it.pack()

lbl_info = tk.Label(app, text="", font=("Arial", 9), wraplength=350)
lbl_info.pack(side="bottom", pady=20)

app.mainloop()