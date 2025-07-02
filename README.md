<p align="center">
  <img src="https://github.com/coderjokerai/Baba-Vanga-Ai/blob/main/logo/logo.png" width="65%">
</p>

# Baba Vanga Ai

Using Baba Vanga Ai, you can have artificial intelligence predict the results of football matches within the leagues!

Actual 0 = Home Win Predictions
Actual 1 = Draw Predictions
Actual 2 = Away Win Predictions

### Accuracy Score: 0.5525

|Confusion Matrix:|Precision|Recall|F1-Score|Support|
| ------------ | ------------ | ------------ | ------------ | ------------ |
|**0**|2|1|0|1|
|**1**|0|0|0|0|
|**2**|0|0|0|0|
|**Accuracy**|||0.55|1238|
|**Macro AVG**|0.48|0.46|0.41|1238|
|**Weighted AVG**|0.50|0.55|0.48|1238|
 

<img src="https://github.com/coderjokerai/Baba-Vanga-Ai/blob/main/logo/1.png">
<img src="https://github.com/coderjokerai/Baba-Vanga-Ai/blob/main/logo/2.png">

## Local Installation (Anaconda)
    conda create -n baba-vanga-ai python=3.11
    conda activate baba-vanga-ai
	git clone https://github.com/coderjokerai/Baba-Vanga-Ai.git
	cd baba-vanga-ai
	pip install -r requirements.txt
	python run.py
## Local Installation
Install Python Version 3.11

	git clone https://github.com/coderjokerai/Baba-Vanga-Ai.git
	cd baba-vanga-ai
	pip install -r requirements.txt
	python run.py
## Google Colab Usage
Download <a href="https://github.com/coderjokerai/Baba-Vanga-Ai/blob/main/Baba_Vanga_Ai.ipynb">baba_vanga_ai.ipynb</a> file and run on Google Colab.



## Accuracy Graphics
**Home Team Wins (0) Actual Outcome Distribution According to Probability Range:**

|prob_range_1|Total in Range|Actual 0|Actual 1|Actual 2|
| ------------ | ------------ | ------------ | ------------ | ------------ |
|**40-50%**|360|166|97|97|
|**50-60%**|231|136|59|36|
|**60-70%**|135|104|20|11|
|**70%+**|47|38|6|3|

<img src="https://github.com/coderjokerai/Baba-Vanga-Ai/blob/main/logo/3.png">

**Draw (1) Actual Outcome Distribution According to Probability Range:**

|prob_range_1|Total in Range|Actual 0|Actual 1|Actual 2|
| ------------ | ------------ | ------------ | ------------ | ------------ |
|**40-50%**|2|1|0|1|
|**50-60%**|0|0|0|0|
|**60-70%**|0|0|0|0|
|**70%+**|0|0|0|0|

<img src="https://github.com/coderjokerai/Baba-Vanga-Ai/blob/main/logo/4.png">

**Away Team Wins (2) Actual Outcome Distribution According to Probability Range:**

|prob_range_1|Total in Range|Actual 0|Actual 1|Actual 2|
| ------------ | ------------ | ------------ | ------------ | ------------ |
|**40-50%**|144|25|25|94|
|**50-60%**|64|8|13|43|
|**60-70%**|14|1|2|11|
|**70%+**|3|0|0|3|

<img src="https://github.com/coderjokerai/Baba-Vanga-Ai/blob/main/logo/5.png">

