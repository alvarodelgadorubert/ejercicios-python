import platform

info_sistema: dict[str, str] = {
    "sistema": platform.system(),
    "version": platform.version(),
    "nodo": platform.node(),
    "procesador": platform.processor()
}

valores_ordenados: list[str] = sorted(list(info_sistema.values()))
print(valores_ordenados)