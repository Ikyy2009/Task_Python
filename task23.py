class Stack:
    def __init__(self):
        self.stack = []  # Inisialisasi stack kosong
    
    # Menambahkan elemen ke stack (push)
    def push(self, item):
        self.stack.append(item)
        print(f"{item} telah ditambahkan ke stack.")
    
    # Menghapus elemen dari stack (pop)
    def pop(self):
        if not self.is_empty():  # Memeriksa apakah stack kosong
            removed_item = self.stack.pop()
            print(f"{removed_item} telah dihapus dari stack.")
            return removed_item
        else:
            print("Stack kosong, tidak ada elemen yang dapat dihapus.")
            return None
    
    # Melihat elemen teratas stack (peek)
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack kosong.")
            return None
    
    # Memeriksa apakah stack kosong
    def is_empty(self):
        return len(self.stack) == 0
    
    # Menampilkan isi stack
    def display(self):
        if self.is_empty():
            print("Stack kosong.")
        else:
            print("Isi stack:", self.stack)

# Penggunaan Stack
stack = Stack()

# Menambahkan elemen ke stack
stack.push(10)
stack.push(20)
stack.push(30)

# Menampilkan elemen teratas stack
print("Elemen teratas stack:", stack.peek())

# Menampilkan seluruh stack
stack.display()

# Menghapus elemen dari stack
stack.pop()

# Menampilkan stack setelah pop
stack.display()

# Memeriksa apakah stack kosong
if stack.is_empty():
    print("Stack kosong.")
else:
    print("Stack tidak kosong.")
