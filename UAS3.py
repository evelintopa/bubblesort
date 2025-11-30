
# -----------------------------
# PROGRAM BUBBLESORT (DESCENDING)
# -----------------------------
def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] < arr[j+1]:   # tukar agar nilai besar di depan
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# -----------------------------
# EKSEKUSI PROGRAM
# -----------------------------
if __name__ == "__main__":
    # Menjalankan program stack
  

    # Data yang akan diurutkan
    data = [15, 45, 32, 22, 66, 75, 10, 17, 9]
    print("\n=== BUBBLESORT DESCENDING ===")
    print("Data sebelum diurutkan:", data)

    hasil = bubble_sort_desc(data)
    print("Data setelah diurutkan (besar → kecil):", hasil)
