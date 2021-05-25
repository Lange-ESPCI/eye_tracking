# Configuration de la Jetson Nano

## Installation des bibliothèques de vision assistée par ordinateur

Tuto :

(https://www.pyimagesearch.com/2020/03/25/how-to-configure-your-nvidia-jetson-nano-for-computer-vision-and-deep-learning/)[https://www.pyimagesearch.com/2020/03/25/how-to-configure-your-nvidia-jetson-nano-for-computer-vision-and-deep-learning/]

Installation de TensorFlow 1.15 et non 1.13 car version de jetpack plus récente (sinon crash)

Version utilisée :

- cmake 3.20.2
- opencv 4.1.2
- scipy 1.3.3
- protobuf 3.6.1

## Scripts

- `acquire.py` : Camera -> test.mp4
- `reader.py` : Lecture image par image d'un fichier mp4
- `test_fps.sh` : Permet de vérifier le framerate de la camera
- `view.sh` : Voir en direct la sortie de la caméra

## Recompilation du driver IMX219 pour la caméra

Utilisation de l'image : `tegra210-p3448-0000-p3449-0000-a02.dtb`
