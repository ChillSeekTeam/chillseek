import os

images = [f for f in os.listdir('data/images/schools') if f.endswith('.png') and 'Building ' in f]
delete_images = [f for f in os.listdir('data/images/schools') if not f in images]


if __name__ == '__main__':
    for image in delete_images:
        os.remove(f'data/images/schools/{image}')
