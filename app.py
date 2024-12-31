from image import ImageProcessor


if __name__ == "__main__":
    # Imagem de exemplo: uma matriz 3x3 RGB
    sample_image = [
        [[255, 0, 0], [0, 255, 0], [0, 0, 255]],  # Linha 1
        [[123, 123, 123], [200, 200, 200], [50, 50, 50]],  # Linha 2
        [[255, 255, 255], [0, 0, 0], [128, 128, 128]]  # Linha 3
    ]

    # Criar o processador de imagem
    processor = ImageProcessor(sample_image)

    # Binarização
    threshold = 128
    binary_result = processor.binarize(threshold)
    print("Imagem Binarizada:")
    for row in binary_result:
        print(row)

    # Tons de cinza
    grayscale_result = processor.to_grayscale()
    print("\nImagem em Tons de Cinza:")
    for row in grayscale_result:
        print(row)
