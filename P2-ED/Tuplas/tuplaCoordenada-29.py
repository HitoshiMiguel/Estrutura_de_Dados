def media_coordenadas(coordenadas):
    soma_x = sum(x for x, y in coordenadas)
    soma_y = sum(y for x, y in coordenadas)
    media_x = soma_x / len(coordenadas)
    media_y = soma_y / len(coordenadas)
    return (media_x, media_y)

coordenadas = [(1, 2), (3, 4), (5, 6), (7, 8)]
media = media_coordenadas(coordenadas)
print(f"As médias das coordenadas são: {media}")
