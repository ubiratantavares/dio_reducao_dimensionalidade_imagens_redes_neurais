class ImageProcessor:
    def __init__(self, image):
        """
        Inicializa o processador de imagens com uma matriz representando a imagem RGB.
        :param image: Lista de listas representando a imagem em RGB.
        """
        self.image = image

    def binarize(self, threshold=128):
        """
        Binariza a imagem com base em um limiar.
        Os valores resultantes serão 0 (preto) ou 255 (branco).
        :param threshold: Valor de limiar para binarização (padrão = 128).
        :return: Imagem binarizada (lista de listas).
        """
        height = len(self.image)
        width = len(self.image[0])
        binary_image = []

        for i in range(height):
            row = []
            for j in range(width):
                # Calcula o brilho médio do pixel (média dos valores RGB)
                pixel = self.image[i][j]
                brightness = sum(pixel) // 3
                # Aplica a binarização
                row.append(255 if brightness >= threshold else 0)
            binary_image.append(row)

        return binary_image

    def to_grayscale(self):
        """
        Converte a imagem para tons de cinza (0 a 255).
        Cada pixel será substituído pelo valor médio dos seus componentes RGB.
        :return: Imagem em tons de cinza (lista de listas).
        """
        height = len(self.image)
        width = len(self.image[0])
        grayscale_image = []

        for i in range(height):
            row = []
            for j in range(width):
                # Calcula o brilho médio do pixel (média dos valores RGB)
                pixel = self.image[i][j]
                brightness = sum(pixel) // 3
                row.append(brightness)
            grayscale_image.append(row)

        return grayscale_image
