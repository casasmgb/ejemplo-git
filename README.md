## Comandos Básicos de Git
## 1. git init

El comando `git init` se utiliza para inicializar un nuevo repositorio Git en un directorio local. Esto crea un nuevo subdirectorio llamado `.git`, que contiene todos los archivos necesarios para el control de versiones.

## 2. git clone [URL]

El comando `git clone [URL]` se utiliza para clonar un repositorio Git existente desde una URL remota a tu directorio local. Descarga una copia completa del repositorio, incluyendo todo el historial de cambios.

## 3. git log

El comando `git log` muestra un registro detallado de todos los commits en el repositorio. Proporciona información sobre el autor del commit, la fecha y la hora del commit, y el mensaje asociado con el commit.

## 4. git add [archivo]

El comando `git add [archivo]` se utiliza para añadir archivos al área de preparación (staging area) para ser incluidos en el próximo commit. Puedes añadir archivos específicos (`git add archivo`) o todos los archivos modificados (`git add .`).

## 5. git commit -m "mensaje"

El comando `git commit -m "[mensaje]"` se utiliza para confirmar los cambios en el repositorio, creando un nuevo commit con los archivos añadidos previamente al área de preparación. El mensaje entre comillas describe los cambios realizados en el commit.

## 6. git push [ORIGEN] [RAMA DESTINO]

El comando `git push` se utiliza para enviar los commits locales al repositorio remoto asociado. Actualiza el historial de cambios en el servidor remoto y comparte tus cambios con otros colaboradores.

## 7. git pull [ORIGEN] [RAMA DESTINO]

El comando `git pull` se utiliza para descargar los cambios desde el repositorio remoto y fusionarlos con tu rama local. Es útil para mantener tu repositorio local actualizado con los cambios realizados por otros colaboradores.

## 8. git merge [RAMA ORIGEN]

El comando `git merge [RAMA DESTINO]` se utiliza para fusionar los cambios de una rama específica en tu rama actual. Combina el historial de cambios de la rama especificada con el historial de cambios de tu rama actual.

## 9. git status

El comando `git status` se utiliza para mostrar el estado actual del repositorio, incluyendo los archivos modificados, los archivos no seguimiento, y los archivos listos para ser confirmados.

## 10. git branch

El comando `git branch` se utiliza para mostrar una lista de las ramas locales en tu repositorio. La rama actual está resaltada con un asterisco (`*`).

## 11. git checkout [RAMA DESTINO]

El comando `git checkout [RAMA DESTINO]` se utiliza para cambiar a una rama específica en tu repositorio local. Te permite trabajar en diferentes ramas para desarrollar funcionalidades independientes o experimentar con cambios.

## 12. git config user.name

El comando `git config user.name` se utiliza para configurar el nombre de usuario que se utilizará para los commits en Git. Esto es importante para identificar quién realizó cada cambio en el repositorio.

## 13. git config user.email

El comando `git config user.email` se utiliza para configurar la dirección de correo electrónico que se utilizará para los commits en Git. Esto es importante para asociar cada commit con una dirección de correo electrónico específica.

## 14. git remote

El comando `git remote` se utiliza para mostrar los repositorios remotos configurados para tu repositorio local. Proporciona información sobre los nombres y las URL de los repositorios remotos asociados.

Espero que esta descripción detallada te sea útil para entender el propósito y el uso de cada uno de estos comandos en Git.
