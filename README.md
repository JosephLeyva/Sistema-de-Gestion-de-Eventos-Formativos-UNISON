# Sistema-de-Gestion-de-Eventos-Formativos-UNISON
Web Application Project for Objet Oriented Analysis and Design subject

------------------------------------------------------------------
# Instalar un Virtual Environment (Recomendación)
Un entorno virtual es un lugar en su sistema donde puede instalar paquetes y aislarlos de todos los demás paquetes de Python.
Es recomendable crear un entorno virtual en la carpeta donde estaremos trabajando
```
# Primero tenemos que instalar virtualenv
pip install virtualenv

# Luego creamos el virtual environment con el nombre que queramos
virtualenv cc_env
```
## Activar el Virtual Environment
```
cc_env\scripts\activate
```
Una vez activado, podemos instalar Django ahí
Para verificar que lo hemos activado, se verá el nombre del virtualenv antes de la ruta
![image](https://user-images.githubusercontent.com/43888961/139622813-49883cca-3035-48e6-8fea-1760de5c9d46.png)

## Desactivar Virtual Environment
Para desactivar el entorno virtual y volver a la cmd principal ejecutamos:
```
cc_env\scripts\deactivate
```

-------------------------------------------------------------------
# Instalar Django
## Requisitos
Tener `python` y `pip` instalado en la computadora

## Checar Versión
Primero chequemos que tenemos Django instalado:
`python -m django --version`

Si, tenemos Django instalado, sale la versión de su instalación. Si no es así, saldrá un error que dice  `No module named django`

## Instalación
`python -m pip install Django`
