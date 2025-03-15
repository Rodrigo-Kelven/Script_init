import os

def create_init_files(base_dir):
    # Percorre todos os diretórios e subdiretórios
    for dirpath, dirnames, filenames in os.walk(base_dir):
        # Verifica se o __init__.py já existe
        if '__init__.py' not in filenames:
            # Cria o arquivo __init__.py
            init_file_path = os.path.join(dirpath, '__init__.py')
            with open(init_file_path, 'w') as init_file:
                init_file.write('# This file indicates that the directory is a Python package\n')
            print(f'Created: {init_file_path}')

if __name__ == '__main__':
    # Defina o diretório base onde você deseja adicionar os __init__.py
    base_directory = 'src'  # Altere para o caminho desejado
    create_init_files(base_directory)
