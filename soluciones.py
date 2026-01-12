"""
Archivo con soluciones completas para los ejercicios 1..100.
Cada solución incluye un comentario indicando a qué ejercicio pertenece.
"""

# Ejercicio 1: Hola mundo
def ejercicio_1():
    print("Hola, mundo!")

# Ejercicio 2: Pedir nombre y saludar
def ejercicio_2(nombre):
    return f"Hola, {nombre}!"

# Ejercicio 3: Sumar dos números
def ejercicio_3(a, b):
    return a + b

# Ejercicio 4: Operaciones matemáticas básicas
def ejercicio_4(a, b):
    return {"suma": a + b, "resta": a - b, "mul": a * b, "div": (a / b) if b != 0 else None}

# Ejercicio 5: Convertir Celsius a Fahrenheit
def ejercicio_5(c):
    return c * 9/5 + 32

# Ejercicio 6: Área de triángulo
def ejercicio_6(base, altura):
    return (base * altura) / 2

# Ejercicio 7: Número par o impar
def ejercicio_7(n):
    return n % 2 == 0

# Ejercicio 8: Número positivo negativo o cero
def ejercicio_8(n):
    if n > 0:
        return "positivo"
    if n < 0:
        return "negativo"
    return "cero"

# Ejercicio 9: Mayor de dos números
def ejercicio_9(a, b):
    return a if a >= b else b

# Ejercicio 10: Mayor de tres números
def ejercicio_10(a, b, c):
    return max(a, b, c)

# Ejercicio 11: Tabla de multiplicar
def ejercicio_11(n, hasta=10):
    return [n * i for i in range(1, hasta + 1)]

# Ejercicio 12: Contar del 1 al 100
def ejercicio_12():
    return list(range(1, 101))

# Ejercicio 13: Suma del 1 al 100
def ejercicio_13():
    return sum(range(1, 101))

# Ejercicio 14: Factorial
def ejercicio_14(n):
    if n < 0:
        raise ValueError("n debe ser no negativo")
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

# Ejercicio 15: Contar vocales
def ejercicio_15(s):
    return sum(1 for ch in s.lower() if ch in 'aeiouáéíóú')

# Ejercicio 16: Invertir cadena
def ejercicio_16(s):
    return s[::-1]

# Ejercicio 17: Palíndromo
def ejercicio_17(s):
    import re
    t = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return t == t[::-1]

# Ejercicio 18: Contar letras sin espacios
def ejercicio_18(s):
    return len(s.replace(' ', ''))

# Ejercicio 19: Reemplazar vocales
def ejercicio_19(s, repl='*'):
    for v in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
        s = s.replace(v, repl)
    return s

# Ejercicio 20: Lista de 10 números
def ejercicio_20(lista):
    if len(lista) != 10:
        raise ValueError("Se requieren exactamente 10 números")
    return list(lista)

# Ejercicio 21: Promedio lista
def ejercicio_21(lista):
    return sum(lista) / len(lista) if lista else 0

# Ejercicio 22: Mayor lista
def ejercicio_22(lista):
    return max(lista)

# Ejercicio 23: Menor lista
def ejercicio_23(lista):
    return min(lista)

# Ejercicio 24: Eliminar duplicados
def ejercicio_24(lista):
    seen = []
    for x in lista:
        if x not in seen:
            seen.append(x)
    return seen

# Ejercicio 25: Ordenar sin sort (selección)
def ejercicio_25(lista):
    arr = list(lista)
    n = len(arr)
    for i in range(n):
        m = i
        for j in range(i+1, n):
            if arr[j] < arr[m]:
                m = j
        arr[i], arr[m] = arr[m], arr[i]
    return arr

# Ejercicio 26: Contar palabras
def ejercicio_26(s):
    return len([w for w in s.split() if w])

# Ejercicio 27: Frecuencia letras
def ejercicio_27(s):
    d = {}
    for ch in s:
        if ch.isalpha():
            d[ch] = d.get(ch, 0) + 1
    return d

# Ejercicio 28: Buscar elemento lista
def ejercicio_28(lista, x):
    try:
        return lista.index(x)
    except ValueError:
        return -1

# Ejercicio 29: Sumar lista
def ejercicio_29(lista):
    return sum(lista)

# Ejercicio 30: Multiplicar lista
def ejercicio_30(lista):
    prod = 1
    for x in lista:
        prod *= x
    return prod

# Ejercicio 31: Filtrar pares
def ejercicio_31(lista):
    return [x for x in lista if x % 2 == 0]

# Ejercicio 32: Filtrar impares
def ejercicio_32(lista):
    return [x for x in lista if x % 2 != 0]

# Ejercicio 33: Diccionario persona
def ejercicio_33(nombre, edad, email):
    return {"nombre": nombre, "edad": edad, "email": email}

# Ejercicio 34: Buscar clave diccionario
def ejercicio_34(d, clave):
    return d.get(clave)

# Ejercicio 35: Lista a diccionario
def ejercicio_35(keys, vals):
    return dict(zip(keys, vals))

# Ejercicio 36: Tabla multiplicar dinámica
def ejercicio_36(n, hasta):
    return [n * i for i in range(1, hasta + 1)]

# Ejercicio 37: Login simple
def ejercicio_37(user, pwd, usuario='admin', clave='1234'):
    return user == usuario and pwd == clave

# Ejercicio 38: Calculadora con menú (funciones básicas)
def ejercicio_38(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b if b != 0 else None
    return None

# Ejercicio 39: Sistema de notas
def ejercicio_39(dic_notas):
    return {alumno: (sum(notas)/len(notas) if notas else 0) for alumno, notas in dic_notas.items()}

# Ejercicio 40: Contar caracteres especiales
def ejercicio_40(s):
    return sum(1 for ch in s if not ch.isalnum() and not ch.isspace())

# Ejercicio 41: Validar email (básico)
def ejercicio_41(s):
    return '@' in s and '.' in s.split('@')[-1]

# Ejercicio 42: Números aleatorios
import random
def ejercicio_42(n, a=0, b=100):
    return [random.randint(a, b) for _ in range(n)]

# Ejercicio 43: Juego adivinar número (retorna numero ganador)
def ejercicio_43(intentos=5, a=1, b=100, seed=None):
    if seed is not None:
        random.seed(seed)
    secreto = random.randint(a, b)
    return secreto

# Ejercicio 44: Generador contraseña
import string
def ejercicio_44(long=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(long))

# Ejercicio 45: Cajero automático
class Ejercicio45Cajero:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            return False
        self.saldo -= cantidad
        return True

    def ver_saldo(self):
        return self.saldo

# Ejercicio 46: Inventario
class Ejercicio46Inventario:
    def __init__(self):
        self.items = {}

    def agregar(self, nombre, cantidad):
        self.items[nombre] = self.items.get(nombre, 0) + cantidad

    def eliminar(self, nombre):
        if nombre in self.items:
            del self.items[nombre]

    def listar(self):
        return dict(self.items)

# Ejercicio 47: Leer archivo
def ejercicio_47(ruta):
    with open(ruta, 'r', encoding='utf-8') as f:
        return f.read()

# Ejercicio 48: Contar líneas archivo
def ejercicio_48(ruta):
    with open(ruta, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)

# Ejercicio 49: Buscar palabra archivo
def ejercicio_49(ruta, palabra):
    lines = []
    with open(ruta, 'r', encoding='utf-8') as f:
        for i, l in enumerate(f, 1):
            if palabra in l:
                lines.append((i, l.rstrip('\n')))
    return lines

# Ejercicio 50: Listas archivo
def ejercicio_50(ruta):
    with open(ruta, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]

# Ejercicio 51: Número primo
def ejercicio_51(n):
    if n < 2:
        return False
    if n % 2 == 0 and n != 2:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

# Ejercicio 52: Decimal a binario
def ejercicio_52(n):
    return bin(n)[2:]

# Ejercicio 53: Binario a decimal
def ejercicio_53(s):
    return int(s, 2)

# Ejercicio 54: Burbuja
def ejercicio_54(lista):
    arr = list(lista)
    n = len(arr)
    changed = True
    while changed:
        changed = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                changed = True
    return arr

# Ejercicio 55: Inserción
def ejercicio_55(lista):
    arr = list(lista)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Ejercicio 56: Búsqueda binaria
def ejercicio_56(lista, x):
    lo, hi = 0, len(lista)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if lista[mid] == x:
            return mid
        if lista[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# Ejercicio 57: Clase Persona
class ejercicio_57_Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

# Ejercicio 58: Clase Estudiante
class ejercicio_58_Estudiante(ejercicio_57_Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso
        self.notas = []

    def agregar_nota(self, n):
        self.notas.append(n)

    def promedio(self):
        return sum(self.notas)/len(self.notas) if self.notas else 0

# Ejercicio 59: Cuenta bancaria
class ejercicio_59_Cuenta:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, c):
        self.saldo += c

    def retirar(self, c):
        if c > self.saldo:
            raise ValueError('Saldo insuficiente')
        self.saldo -= c

# Ejercicio 60: Vehículo / herencia
class ejercicio_60_Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def info(self):
        return f"Vehículo: {self.marca}"

class ejercicio_60_Coche(ejercicio_60_Vehiculo):
    def __init__(self, marca, puertas):
        super().__init__(marca)
        self.puertas = puertas

# Ejercicio 61: Excepciones
def ejercicio_61_dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

# Ejercicio 62: Módulo propio (ejemplo)
def ejercicio_62_saludo():
    return "Hola desde el módulo"

# Ejercicio 63: Matriz 3x3
def ejercicio_63_crear():
    return [[0]*3 for _ in range(3)]

# Ejercicio 64: Suma matrices
def ejercicio_64_sum(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

# Ejercicio 65: Multiplicación matrices
def ejercicio_65_mul(a, b):
    m, p = len(a), len(b[0])
    n = len(b)
    res = [[0]*p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                res[i][j] += a[i][k] * b[k][j]
    return res

# Ejercicio 66: Transponer matriz
def ejercicio_66_transponer(m):
    return [list(row) for row in zip(*m)]

# Ejercicio 67: Menú avanzado (función de ejemplo)
def ejercicio_67_opcion(op):
    return f"Opción {op} seleccionada"

# Ejercicio 68: Sistema tareas
class ejercicio_68_SistemaTareas:
    def __init__(self):
        self.tareas = {}
        self.next_id = 1

    def añadir(self, desc):
        tid = self.next_id
        self.tareas[tid] = {"desc": desc, "hecho": False}
        self.next_id += 1
        return tid

    def marcar_hecho(self, tid):
        if tid in self.tareas:
            self.tareas[tid]['hecho'] = True

# Ejercicio 69: Registro usuario (almacena en dict)
class ejercicio_69_Reg:
    def __init__(self):
        self.users = {}

    def registrar(self, user, pwd):
        self.users[user] = pwd

    def existe(self, user):
        return user in self.users

# Ejercicio 70: Login con archivo
def ejercicio_70_login_archivo(ruta, user, pwd):
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            for line in f:
                u, p = line.strip().split(',')
                if u == user and p == pwd:
                    return True
    except FileNotFoundError:
        return False
    return False

# Ejercicio 71: Agenda telefónica
class ejercicio_71_Agenda:
    def __init__(self):
        self.contactos = {}

    def agregar(self, nombre, telefono):
        self.contactos[nombre] = telefono

    def buscar(self, nombre):
        return self.contactos.get(nombre)

# Ejercicio 72: API Request (urllib)
import urllib.request
import json
def ejercicio_72_request(url):
    try:
        with urllib.request.urlopen(url, timeout=5) as r:
            return r.read().decode('utf-8')
    except Exception:
        return None

# Ejercicio 73: JSON
def ejercicio_73_serializar(obj):
    return json.dumps(obj)

def ejercicio_73_deserializar(s):
    return json.loads(s)

# Ejercicio 74: Cronómetro
import time
class ejercicio_74_Cronometro:
    def __init__(self):
        self.t0 = None

    def start(self):
        self.t0 = time.time()

    def stop(self):
        return time.time() - self.t0 if self.t0 else None

# Ejercicio 75: Temporizador
def ejercicio_75_temporizador(segundos):
    time.sleep(segundos)
    return True

# Ejercicio 76: Palabras más usadas
from collections import Counter
def ejercicio_76_mas_usadas(texto, n=5):
    words = [w.strip().lower() for w in texto.split() if w]
    return Counter(words).most_common(n)

# Ejercicio 77: Detector spam (heurístico)
def ejercicio_77_detector(texto):
    spam_words = ['gratis', 'oferta', 'compra', 'click', 'dinero']
    t = texto.lower()
    return any(w in t for w in spam_words)

# Ejercicio 78: Conversor moneda
def ejercicio_78_conversor(cantidad, tasa):
    return cantidad * tasa

# Ejercicio 79: Encriptar texto simple (César)
def ejercicio_79_cesar(texto, d):
    res = []
    for ch in texto:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            res.append(chr((ord(ch) - ord(base) + d) % 26 + ord(base)))
        else:
            res.append(ch)
    return ''.join(res)

# Ejercicio 80: Chatbot básico
def ejercicio_80_chatbot(m):
    m = m.lower()
    if 'hola' in m:
        return 'Hola! ¿En qué puedo ayudarte?'
    if 'adiós' in m or 'chao' in m:
        return '¡Adiós!'
    return 'Lo siento, no entiendo.'

# Ejercicio 81: Sistema tickets
class ejercicio_81_Tickets:
    def __init__(self):
        self.tickets = {}
        self.next_id = 1

    def crear(self, descripcion):
        tid = self.next_id
        self.tickets[tid] = {'desc': descripcion, 'estado': 'open'}
        self.next_id += 1
        return tid

    def cerrar(self, tid):
        if tid in self.tickets:
            self.tickets[tid]['estado'] = 'closed'

# Ejercicio 82: Piedra papel tijera
def ejercicio_82_rps(a, b):
    reglas = {'piedra': 'tijera', 'tijera': 'papel', 'papel': 'piedra'}
    if a == b:
        return 'empate'
    return 'jugador1' if reglas.get(a) == b else 'jugador2'

# Ejercicio 83: Ahorcado (motor básico)
class ejercicio_83_Ahorcado:
    def __init__(self, palabra):
        self.palabra = palabra
        self.intentos = set()

    def adivinar(self, letra):
        self.intentos.add(letra)
        return all(c in self.intentos for c in self.palabra)

# Ejercicio 84: Dados
def ejercicio_84_tirar(n=2):
    return [random.randint(1, 6) for _ in range(n)]

# Ejercicio 85: Analizador rendimiento
def ejercicio_85_medir(func, args=(), reps=5):
    tiempos = []
    for _ in range(reps):
        t0 = time.time()
        func(*args)
        tiempos.append(time.time() - t0)
    return {'min': min(tiempos), 'max': max(tiempos), 'avg': sum(tiempos)/len(tiempos)}

# Ejercicio 86: Leer CSV
import csv
def ejercicio_86_leer_csv(ruta):
    with open(ruta, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

# Ejercicio 87: Estadísticas CSV
def ejercicio_87_stats(filas, columna):
    vals = [float(r[columna]) for r in filas if r.get(columna) not in (None, '')]
    vals.sort()
    n = len(vals)
    mean = sum(vals)/n if n else 0
    median = vals[n//2] if n else 0
    var = sum((x-mean)**2 for x in vals)/n if n else 0
    return {'mean': mean, 'median': median, 'std': var**0.5}

# Ejercicio 88: Limpieza dataset
def ejercicio_88_clean(filas):
    cleaned = []
    seen = set()
    for r in filas:
        nr = {k: (v.strip() if isinstance(v, str) else v) for k, v in r.items()}
        key = tuple(nr.items())
        if key in seen:
            continue
        seen.add(key)
        cleaned.append(nr)
    return cleaned

# Ejercicio 89: Normalizar lista (min-max)
def ejercicio_89_normalizar(lista):
    mi, ma = min(lista), max(lista)
    if ma == mi:
        return [0.0 for _ in lista]
    return [(x-mi)/(ma-mi) for x in lista]

# Ejercicio 90: Regresión lineal manual (1D)
def ejercicio_90_regresion(xs, ys):
    n = len(xs)
    mx = sum(xs)/n
    my = sum(ys)/n
    num = sum((xs[i]-mx)*(ys[i]-my) for i in range(n))
    den = sum((xs[i]-mx)**2 for i in range(n))
    b1 = num/den if den else 0
    b0 = my - b1*mx
    return b0, b1

# Ejercicio 91: kNN manual
import math
def ejercicio_91_knn(train_X, train_y, x, k=3):
    d = [(math.dist(x, tx), ty) for tx, ty in zip(train_X, train_y)]
    d.sort(key=lambda t: t[0])
    votos = {}
    for _, label in d[:k]:
        votos[label] = votos.get(label, 0) + 1
    return max(votos.items(), key=lambda kv: kv[1])[0]

# Ejercicio 92: k-means manual (2D)
def ejercicio_92_kmeans(points, k=2, iters=10):
    centers = random.sample(points, k)
    for _ in range(iters):
        clusters = [[] for _ in range(k)]
        for p in points:
            idx = min(range(k), key=lambda i: math.dist(p, centers[i]))
            clusters[idx].append(p)
        new_centers = []
        for c in clusters:
            if c:
                x = sum(p[0] for p in c)/len(c)
                y = sum(p[1] for p in c)/len(c)
                new_centers.append((x, y))
            else:
                new_centers.append(random.choice(points))
        centers = new_centers
    return centers, clusters

# Ejercicio 93: Distancia euclidiana
def ejercicio_93_dist(a, b):
    return math.dist(a, b)

# Ejercicio 94: Outliers (z-score)
def ejercicio_94_outliers(lista, umbral=3):
    n = len(lista)
    mean = sum(lista)/n
    std = (sum((x-mean)**2 for x in lista)/n)**0.5
    return [x for x in lista if abs((x-mean)/std) > umbral] if std else []

# Ejercicio 95: Clasificador binario simple (perceptrón)
def ejercicio_95_perceptron_train(X, y, iters=10, lr=0.1):
    m = len(X[0])
    w = [0.0]*m
    b = 0.0
    for _ in range(iters):
        for xi, yi in zip(X, y):
            activation = sum(wi*xi[j] for j, wi in enumerate(w)) + b
            pred = 1 if activation >= 0 else 0
            err = yi - pred
            for j in range(m):
                w[j] += lr * err * xi[j]
            b += lr * err
    return w, b

# Ejercicio 96: Mini red neuronal conceptual (una capa oculta, sin librerías)
import math
def _sig(x):
    return 1/(1+math.exp(-x))

def ejercicio_96_mini_red(X, y, hidden=3, epochs=100, lr=0.1):
    n_features = len(X[0])
    # inicializar pesos
    wh = [[random.uniform(-0.5, 0.5) for _ in range(n_features)] for _ in range(hidden)]
    bh = [0.0]*hidden
    wo = [random.uniform(-0.5, 0.5) for _ in range(hidden)]
    bo = 0.0
    for _ in range(epochs):
        for xi, yi in zip(X, y):
            # forward
            zh = [sum(w*h for w,h in zip(wh_row, xi)) + b for wh_row, b in zip(wh, bh)]
            ah = [_sig(z) for z in zh]
            zo = sum(w*a for w,a in zip(wo, ah)) + bo
            ao = _sig(zo)
            # backward (gradientes simples)
            d_ao = ao - yi
            for i in range(len(wo)):
                wo[i] -= lr * d_ao * ah[i]
            bo -= lr * d_ao
            for j in range(len(wh)):
                d_ah = d_ao * wo[j] * ah[j] * (1 - ah[j])
                for k in range(n_features):
                    wh[j][k] -= lr * d_ah * xi[k]
                bh[j] -= lr * d_ah
    return {'wh': wh, 'bh': bh, 'wo': wo, 'bo': bo}

# Ejercicio 97: Dataset sintético
def ejercicio_97_generar(n=100):
    pts = []
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = 2*x + random.uniform(-0.5, 0.5)
        pts.append((x, y))
    return pts

# Ejercicio 98: Recomendador simple (popularidad)
def ejercicio_98_recomendar(user_items, k=5):
    count = {}
    for items in user_items.values():
        for it in items:
            count[it] = count.get(it, 0) + 1
    popular = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return [it for it, _ in popular[:k]]

# Ejercicio 99: Sentimiento básico
def ejercicio_99_sentimiento(texto):
    positivos = {'bien', 'genial', 'excelente', 'bueno', 'feliz'}
    negativos = {'malo', 'terrible', 'horrible', 'triste', 'mal'}
    s = texto.lower()
    score = sum(1 for w in positivos if w in s) - sum(1 for w in negativos if w in s)
    return 'positivo' if score>0 else ('negativo' if score<0 else 'neutro')

# Ejercicio 100: Proyecto IA que aprende datos (regresión simple cerrada)
def ejercicio_100_proyecto(xs, ys):
    # Normalizar
    xs_n = ejercicio_89_normalizar(xs)
    b0, b1 = ejercicio_90_regresion(xs_n, ys)
    return b0, b1

if __name__ == '__main__':
    # Ejemplo rápido: ejecutar algunos ejercicios
    print('Ej1:')
    ejercicio_1()
    print('Ej5:', ejercicio_5(0))
    print('Ej14:', ejercicio_14(5))
    print('Ej44:', ejercicio_44(8))
