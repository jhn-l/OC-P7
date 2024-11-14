# Utiliser debian comme image de base
FROM debian:12-slim

ENV PYTHONUNBUFFERED=1
ENV LANG=fr_FR.UTF-8

# Définir les répertoires runtime et data de Jupyter dans des emplacements accessibles
# ENV JUPYTER_RUNTIME_DIR=/tmp/jupyter/runtime
# ENV JUPYTER_DATA_DIR=/tmp/jupyter/data

WORKDIR /code/

# Installer les paquets de base
RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-utils nano wkhtmltopdf sudo locales \
    python3 python3-dev python3-pip python3-venv \
    ipython3 vim git curl libgomp1 && \
    rm -rf /var/lib/apt/lists/* && \
    localedef -i fr_FR -c -f UTF-8 -A /usr/share/locale/locale.alias fr_FR.UTF-8 

# Configurer et activer l'environnement virtuel
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copier et installer les dépendances depuis le fichier requirements.txt
COPY ./data/requirements.txt /code/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /code/requirements.txt

# Générer la configuration de Jupyter Notebook
RUN jupyter notebook --generate-config

# Créer les répertoires nécessaires et leur donner les permissions d'écriture
RUN mkdir -p /tmp/jupyter/runtime /tmp/jupyter/data && \
    chmod -R 777 /tmp/jupyter


# Copier le fichier de configuration Jupyter
COPY ./data/config.txt /tmp/config.txt
RUN cat /tmp/config.txt >> /root/.jupyter/jupyter_notebook_config.py

# Commande par défaut pour lancer Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root"]
