try:
    with open("system_report.txt", "r") as f_in:
        contenido = f_in.read()
    
    with open("system_report_history.txt", "a") as f_out:
        f_out.write(contenido)
        f_out.write("-" * 20 + "\n")
except FileNotFoundError:
    print("Debes ejecutar primero el ejercicio 1.")