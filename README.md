# Tech-Enhanced-AI-Interview-Learning-Platform
This project introduces an advanced machine learning model designed to generate a wide range of interview questions tailored to specific topics based on an individual's resume, all while maintaining a deep level of conversation. Furthermore, we incorporate cutting-edge natural language processing (NLP) algorithms to analyse spoken responses, pinpointing grammatical errors, and providing precise corrections post-interview. Additionally, we employ state-of-the-art speech processing techniques, including Automatic Speech Recognition (ASR), to assess learners' speaking pace, detect variations, and provide timely feedback for improvement. The goal of our model is to boost its adaptability and effectiveness across diverse topics and communication styles.

![FLOWCHART](https://github.com/galactic-me/Tech-Enhanced-AI-Interview-Learning-Platform/assets/81435698/3200f4bb-a3ff-4fff-968b-28081a188bcb)



## DATASET PREPARATION
We combined various datasets containing Questions and Answers for various Job profiles such as Software, Business, Language and AI-ML Roles. 
We added context to them; which was well required by a T5 Transformer to learn and generate Questions.

## OVERVIEW

-**RESUME SCANNING and CLASSIFICATION**\
-**QUESTION GENERATION**\
-**ASR and SPEECH ANALYSES**\
-**GRAMMAR CORRECTION(using API)**\
-**EVALUATION(BLEU SCORES)**

**Resume Scanning and Classification**:  User will input a pdf of his/her resume. NER is used to identify keywords based on the skills and projects mentioned in resume. Then using used Multinomial Naive Bayes, Nearest K-Neighbour Classification to classify the resumes into various job profiles.

![WhatsApp Image 2024-04-13 at 00 47 16_94d37725](https://github.com/galactic-me/Tech-Enhanced-AI-Interview-Learning-Platform/assets/126558668/4ca540a3-ca3e-4aca-bfd9-7911dfbcf212)

**Question Generation**: Based on the job Profile, it will generate questions.For Question Generation, we have fine tuned a T5 Transformer for text-to-text generation. The Dataset consists of 4 columns: Questions, Answers, Job Profiles and Context. 

  **T5 Transformer** (**T**ext-**T**o-**T**ext **T**ransfer **T**ransformer)
   We fine tuned a T5 Transformer , which is an encoder-decoder model pre-trained on Squad Dataset. It works well on a variety of tasks that include text-to-text generation. It takes input in form of text and generates output in the form of text.
   ![image](https://github.com/galactic-me/Tech-Enhanced-AI-Interview-Learning-Platform/assets/126558668/143db14b-3a8d-4920-8aa3-0507a715f2aa)

**ASR and SPEECH ANALYSES**: Used pyAudio to convert audio into text to generate Follow-Up Questions and then it uses the candidate speech to generate follow up questions using the same Question Generation Model. We also use this audio to identify grammatical errors using a python library:language_tool_python.Automatic Speech Recognition (ASR) is a complex process that converts spoken language into written text. It encompasses several stages including audio pre-processing, feature extraction, phoneme and word mapping, and statistical modeling to determine the most probable sequence of words. The outcome of ASR is the transcribed text, offering a valuable tool for accurately capturing and interpreting spoken information in various applications.

**EVALUATION**:BLEU Scores are used to evaluate the model for generated text.
BLEU Scores:It is a number between zero and one that measures the similarity of the machine-generated text with human generated text. A score of 0.6 to 0.7 is considered the standard.




