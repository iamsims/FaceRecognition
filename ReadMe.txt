A smart home automation tool for Locus 2020 by implementation of Siamese Model to recognize faces.

To run and use for face recognition, clone  the repo and,


For Windows:
i.download python 3.7.4
ii.make virtualenv by specifying path to the python by the given command:
   virtualenv -p PATH ENVIRONMENTNAME 
   e.g. virtualenv -p "C:\Python37_64\python.exe" SiamseseEnv
iii.install requirements by following command:
   pip install -r requirements.txt
iv.run main file
v. add contrastive loss if contrastive loss is not found in losses.py file :

def contrastive_loss(y_true, y_pred):
    margin = 1
    return K.mean(y_true * K.square(y_pred) + (1 - y_true) * K.square(K.maximum(margin - y_pred, 0)))


For Linux:
i.Install virtual environment with python = 3.7
 for Debian:  sudo apt install python3.7-venv
              python3.7 -m venv env37
              source env37/bin/activate

ii.install requirements by following command:
   pip install -r requirements.txt
iii.run main file 
iv. add contrastive loss if contrastive loss is not found in losses.py file :

def contrastive_loss(y_true, y_pred):
    margin = 1
    return K.mean(y_true * K.square(y_pred) + (1 - y_true) * K.square(K.maximum(margin - y_pred, 0)))

