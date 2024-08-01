class TwoStacks:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.top1, self.top2 = -1, size

    def push1(self, value):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = value
        else:
            print(f"Desbordamiento de pila por elemento: {value}")

    def push2(self, value):
        if self.top2 > self.top1 + 1:
            self.top2 -= 1
            self.arr[self.top2] = value
        else:
            print(f"Desbordamiento de pila por elemento: {value}")

    def pop1(self):
        if self.top1 >= 0:
            value = self.arr[self.top1]
            self.arr[self.top1] = None
            self.top1 -= 1
            print(f"El elemento extraido de la pila 1 es: {value}")
            return value
        print("Desbordamiento de pila: No hay elementos para desapilar en la Pila 1")
        return None

    def pop2(self):
        if self.top2 < self.size:
            value = self.arr[self.top2]
            self.arr[self.top2] = None
            self.top2 += 1
            print(f"El elemento extraido de la pila 2 es: {value}")
            return value
        print("Desbordamiento de pila: No hay elementos para desapilar en la Pila 2")
        return None

    def peek1(self):
        if self.top1 >= 0:
            return self.arr[self.top1]
        print("La Pila 1 está vacía")
        return None

    def peek2(self):
        if self.top2 < self.size:
            return self.arr[self.top2]
        print("La Pila 2 está vacía")
        return None

def find_next_greater_elements(arr):
    stack, result = [], [-1] * len(arr)
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result

# Ejemplo de uso
ts = TwoStacks(10)
for val in [5, 15, 25, 6, 7, 8, 9, 10]: ts.push1(val)
for val in [10, 20, 30, 31, 32, 33, 34, 35]: ts.push2(val)
print("Pila 1 tope:", ts.peek1())
print("Pila 2 tope:", ts.peek2())
ts.pop1()
ts.pop2()
print("Pila 1 tope:", ts.peek1())
print("Pila 2 tope:", ts.peek2())

# Prueba de elementos mayores
arr = [11, 13, 21, 3]
next_greater_elements = find_next_greater_elements(arr)
for i, val in enumerate(arr):
    print(f"{val} --> {next_greater_elements[i]}")


"""

def siguiente_elemento_mayor(arr):
    # Inicializar una pila vacía
    pila = []
    # Inicializar el array de resultados con valores de -1
    resultado = [-1] * len(arr)
    
    # Recorrer el array de derecha a izquierda
    for i in range(len(arr) - 1, -1, -1):
        # Desapilar elementos hasta encontrar uno mayor
        while pila and pila[-1] <= arr[i]:
            pila.pop()
        
        # Si la pila no está vacía, el elemento superior es el siguiente mayor
        if pila:
            resultado[i] = pila[-1]
        
        # Apilar el elemento actual
        pila.append(arr[i])
    
    # Imprimir los resultados en el formato especificado
    for i in range(len(arr)):
        print(f"{arr[i]}->{resultado[i]}")

# Probar la función con los ejemplos proporcionados
arr1 = [4, 5, 2, 25]
arr2 = [13, 7, 6, 12]
print(arr1)
print("Salida para arr1:")
siguiente_elemento_mayor(arr1)

print(arr2)
print("\nSalida para arr2:")
siguiente_elemento_mayor(arr2) 
"""
"""
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def __str__(self):
        return ' '.join(map(str, self.items))

def insert_at_bottom(stack, item):
    if stack.is_empty():
        stack.push(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.push(temp)

def reverse_stack(stack):
    if not stack.is_empty():
        temp = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, temp)

# Ejemplo de uso
stack = Stack()
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)

# Mostrar la pila original
print("Pila Original")
print(stack)

# Revertir la pila
reverse_stack(stack)

# Mostrar la pila invertida
print("Pila Invertida")
print(stack)
"""