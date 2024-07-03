import math

# Noktaların tanımlanması
points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

# Öklid mesafesi hesaplama fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append((points[i], points[j], distance))

# Minimum mesafenin bulunması ve yazdırılması
min_distance = min(distances, key=lambda x: x[2])
print(f"Minimum mesafe: {min_distance[2]} birim")
print(f"Bu mesafe {min_distance[0]} ve {min_distance[1]} noktaları arasındadır.")


"""
çıktısı :
Minimum mesafe: 1.4142135623730951 birim
Bu mesafe (0, 0) ve (1, 1) noktaları arasındadır.
"""