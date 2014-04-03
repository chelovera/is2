#!/bin/bash

# Verifica si existe la configuracion del sphinx
if [ ! -f docs/conf.py ]; then
    echo "Configure Sphinx con Pycharm siguiendo los pasos del archivo Sphinx.txt"
    exit
fi

# Crear archivos .rst sobre los modulos
echo "Creando .rst"
sphinx-apidoc -f -o docs/ .

# Cambiar el titulo del archivo modules.rst
cd docs/
echo -e "\nArreglando 'modules.rst'."
sed -i.bak s/^'\.'$/Packages/ modules.rst
sed -i.bak s/^=$/========/ modules.rst


# Crear los archivos html
echo -e "Creando archivos html\n"
make html
