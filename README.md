## A smart home automation tool for Locus 2020 by implementation of Siamese Model to recognize faces.

### Installation
**Cloning the repository For code**:

		git clone https://github.com/simran347/FaceRecognition.git

      

1. #### For Windows:

* Download Python 3.7
* Create the Virtual Environment:
		
		#Creating Virtual Env
		virtualenv -p PATH ENVIRONMENTNAME 
		#Activating virtual env
		\path\to\env\Scripts\activate

* Install dependencies:

		pip install -r requirements.txt


2. #### For Linux:

* Install virtual environment with python = 3.7

		sudo apt install python3.7-venv

* Create the Virtual Environment
		
		#Creating Virtual Env
		python3.7 -m venv env37
		#Activating virtual env
		source env37/bin/activate
 
* Install Dependencies:

		pip install -r requirements.txt 


### Run the program 
1. Run main file  
2. Add contrastive loss if contrastive loss is not found in losses.py file:

`def contrastive_loss(y_true, y_pred):
return K.mean(y_true * K.square(y_pred) + (1 - y_true) * K.square(K.maximum(margin - y_pred, 0)))`
