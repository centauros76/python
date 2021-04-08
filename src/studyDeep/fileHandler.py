import imageio

img_array = imageio.imread('/Users/rene.kwak/Private/5_28by28.png', as_gray=True)

img_data = 255.0 - img_array.reshape(784)
img_data = (img_data / 255.0 * 0.99) + 0.01

print(img_data)