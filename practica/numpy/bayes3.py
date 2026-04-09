total = 100
excel = 60
python_usuarios = 45
ambos = 30

solo_excel = excel - ambos
solo_python = python_usuarios - ambos
excel_o_python = excel + python_usuarios - ambos
ninguno = total - excel_o_python

p_excel_o_python = excel_o_python / total
p_solo_excel = solo_excel / total
p_ninguno = ninguno / total

p_python = python_usuarios / total
p_no_python = 1 - p_python

p_aprueba_dado_python = 0.70
p_aprueba_dado_no_python = 0.20

p_aprueba = (p_aprueba_dado_python * p_python) + (p_aprueba_dado_no_python * p_no_python)

p_python_dado_aprueba = (p_aprueba_dado_python * p_python) / p_aprueba

print("=== RESULTADOS ===")
print(f"a) P(Excel o Python) = {p_excel_o_python}")
print(f"b) P(solo Excel) = {p_solo_excel}")
print(f"c) P(ninguna) = {p_ninguno}")
print(f"d) P(aprobar) = {p_aprueba}")
print(f"e) P(Python | aprobó) = {p_python_dado_aprueba}")