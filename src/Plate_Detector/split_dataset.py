import os
import shutil
from sklearn.model_selection import train_test_split

# Diretório contendo as imagens e os rótulos
images_dir = "src/Plate_Detector/dataset/train/images"
labels_dir = "src/Plate_Detector/dataset/train/labels"

# Listar os arquivos de imagem
image_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg')]

# Divisão dos dados: 80% treino, 10% validação, 10% teste
train_files, test_files = train_test_split(image_files, test_size=0.2, random_state=42)
val_files, test_files = train_test_split(test_files, test_size=0.5, random_state=42)

# Criar as pastas de saída
output_dirs = {
    "train": {"images": "dataset/train/images", "labels": "dataset/train/labels"},
    "val": {"images": "dataset/val/images", "labels": "dataset/val/labels"},
    "test": {"images": "dataset/test/images", "labels": "dataset/test/labels"},
}

for key, paths in output_dirs.items():
    os.makedirs(paths["images"], exist_ok=True)
    os.makedirs(paths["labels"], exist_ok=True)

# Função para mover arquivos de imagem e rótulo
def move_files(file_list, subset):
    for file_name in file_list:
        # Caminho da imagem e rótulo
        image_path = os.path.join(images_dir, file_name)
        label_path = os.path.join(labels_dir, file_name.replace('.jpg', '.txt'))
        
        # Destinos
        dest_image_path = os.path.join(output_dirs[subset]["images"], file_name)
        dest_label_path = os.path.join(output_dirs[subset]["labels"], file_name.replace('.jpg', '.txt'))
        
        # Mover arquivos
        shutil.copy(image_path, dest_image_path)
        if os.path.exists(label_path):  # Caso exista um arquivo de rótulo
            shutil.copy(label_path, dest_label_path)

# Mover os arquivos
move_files(train_files, "train")
move_files(val_files, "val")
move_files(test_files, "test")

print("Divisão completa!")
