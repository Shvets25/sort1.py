import os
import shutil
import sys


def process_folder(folder_path):
    # доступ до папки
    print(f"Processing folder: {folder_path}")




def normalize(filename):
    # Тут реалізуємо функцію normalize
    pass


def process_folder(folder_path):
    images = ('JPEG', 'PNG', 'JPG', 'SVG')
    videos = ('AVI', 'MP4', 'MOV', 'MKV')
    documents = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
    audio = ('MP3', 'OGG', 'WAV', 'AMR')
    archives = ('ZIP', 'GZ', 'TAR')

    # Перебираємо файли та папки в поточній папці
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        # Якщо це папка, рекурсивно обробляємо її
        if os.path.isdir(item_path) and item not in ('archives', 'video', 'audio', 'documents', 'images'):
            process_folder(item_path)

        # Якщо це файл
        elif os.path.isfile(item_path):
            filename, file_extension = os.path.splitext(item)
            normalized_filename = normalize(filename)

            # Якщо розширення відоме, відповідно сортуємо
            if file_extension.upper()[1:] in images:
                target_folder = 'images'
            elif file_extension.upper()[1:] in videos:
                target_folder = 'videos'
            elif file_extension.upper()[1:] in documents:
                target_folder = 'documents'
            elif file_extension.upper()[1:] in audio:
                target_folder = 'audio'
            elif file_extension.upper()[1:] in archives:
                target_folder = 'archives'
                archive_folder = os.path.join(folder_path, target_folder, normalized_filename)
                os.makedirs(archive_folder, exist_ok=True)
                # Тут розпаковуємо архів в архівну папку
                pass
            else:
                target_folder = 'unknown'

            # Переміщуємо файл до відповідної папки
            target_path = os.path.join(folder_path, target_folder, normalized_filename + file_extension)
            shutil.move(item_path, target_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sort.py folder_path")
    else:
        folder_path = sys.argv[1]
        process_folder(folder_path)