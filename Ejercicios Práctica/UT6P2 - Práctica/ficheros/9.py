import datetime

with open("log.txt", "a") as f:
    ahora = datetime.datetime.now()
    f.write(f"Log registrado el: {ahora}\n")