#!/usr/bin/env python
# coding: utf-8

# In[1]:


#creating a function to create a file
def filecreator(filename,text):
    # Open a file for writing
    file = open(filename, "w")

    # Write content to the file
    file.write(text)

    # Close the file
    file.close()


# In[3]:


filename="text1.txt"
text="Artificial Intelligence (AI) has revolutionized various sectors, and one of the most promising areas of its application is healthcare. With its ability to process massive amounts of data, identify patterns, and make predictions, AI is transforming the way medical professionals diagnose, treat, and manage diseases. For instance, AI algorithms can analyze medical images, such as X-rays and MRIs, with remarkable accuracy, aiding in the early detection of conditions like cancer. Furthermore, AI-powered virtual assistants and chatbots are enhancing patient engagement by providing round-the-clock support and answering medical queries. The integration of AI in healthcare not only improves efficiency and precision but also has the potential to personalize treatments based on individual patient data. While there are still challenges to overcome, the rise of AI in healthcare holds great promise for advancing patient care and transforming the future of medicine."
filecreator(filename,text)

filename="text2.txt"
text="Renewable energy has emerged as a pivotal solution in addressing the challenges of climate change and achieving sustainable development. With the world increasingly recognizing the detrimental effects of fossil fuels, the shift towards renewable sources such as solar, wind, and hydropower has gained significant momentum. The adoption of renewable energy not only helps to reduce greenhouse gas emissions but also offers economic and social benefits. By harnessing the power of clean energy, countries can enhance energy security, create job opportunities, and promote local economic growth. Moreover, renewable energy projects often prioritize community engagement and participation, ensuring the inclusion of marginalized groups and promoting social equity. However, while the potential of renewable energy is immense, challenges such as intermittency and infrastructure limitations need to be addressed. Through continued investment, technological advancements, and supportive policies, renewable energy can play a crucial role in driving sustainable development and building a greener future for generations to come."
filecreator(filename,text)

filename="text3.txt"
text="In the increasingly interconnected world of the digital age, cybersecurity has become a critical aspect of our daily lives. With the exponential growth of technology and the widespread use of the internet, protecting our sensitive information and digital assets has become more crucial than ever. Cyberattacks, ranging from data breaches to ransomware attacks, pose significant threats to individuals, businesses, and even nations. The implications of a successful cyberattack can be devastating, including financial loss, reputational damage, and compromised privacy. As our reliance on digital platforms and services continues to expand, it is imperative to prioritize cybersecurity measures. This includes implementing strong passwords, regularly updating software, and employing robust encryption techniques. Furthermore, education and awareness about online risks are essential to empower individuals and organizations to detect and respond to potential threats proactively. By investing in cybersecurity measures and fostering a culture of cyber resilience, we can safeguard our digital infrastructure and ensure a safer and more secure digital future for everyone."
filecreator(filename,text)

filename="text4.txt"
text="The adoption of renewable energy not only helps to reduce greenhouse gas emissions but also offers economic and social benefits. By harnessing the power of clean energy, countries can enhance energy security, create job opportunities, and promote local economic growth. Moreover, renewable energy projects often prioritize community engagement and participation, ensuring the inclusion of marginalized groups and promoting social equity."
filecreator(filename,text)


# In[4]:


#Creating a function for reading a file then return as string
def fileReader(filename):
    # Open the file for reading
    file = open(filename,"r")

    # Read the contents of the file
    content = file.read()

    # Close the file
    file.close()
    return content


# In[5]:


#pulling data from text files then saving to string using filereader function
string1=fileReader("text1.txt")
string2=fileReader("text2.txt")
string3=fileReader("text3.txt")
string4=fileReader("text4.txt")


# In[6]:


#creating a function for removing special characters and some words
import re
def remover(text):
    pattern = r'[^a-zA-Z0-9\s]'  # Regular expression pattern to match special characters
    text = re.sub(pattern, '', text)
    text = text.replace("a ","")
    text = text.replace("the ","")
    text = text.replace("of ","")
    text = text.replace("etc ","")
    text = text.replace("and ","")
    text = text.replace("its ","")
    text = text.replace("has ","")
    text = text.replace("is ","")
    text = text.replace("in ","")
    text = text.replace("for ","")
    text = text.replace("to ","")
    return text


# In[7]:


#using the remover function to sanitize a string
newstring1 = remover(string1)
newstring2 = remover(string2)
newstring3 = remover(string3)
newstring4 = remover(string4)


# In[9]:


#creating a list of string, and using join function to group the strings as string
strings = [newstring1,newstring2,newstring3,newstring4]
allstrings = " ".join(strings)


# In[13]:


#using split function to split all data in string.
#using set function to remove duplicate data.
#to convert as a list we use list function
words = allstrings.split()
unique_words = list(set(words))


# In[124]:


# counting the occurrence of unique words in string
def occurenceCounter(stringOfText,unique_words):
    #unique_words
    string_count=[]
    matching_documents = []

    strings = stringOfText.split()

    for word in unique_words:
        word_count = [word,'0'] 
        string_count.append(word_count)

    for string in strings:
        for i, word_count in enumerate(string_count):
            if string in word_count:
                matching_documents.append(i)

    #ss
    for index in matching_documents:
        string_count[index][1] = str(int(string_count[index][1]) + 1)  # Increment the value of the first element

    newlist={}
    for list in string_count:
        newlist[list[0]]=list[1]
    
    return newlist


# In[29]:


fileOccurence1= occurenceCounter(newstring1,unique_words)
fileOccurence2= occurenceCounter(newstring2,unique_words)
fileOccurence3= occurenceCounter(newstring3,unique_words)
fileOccurence4= occurenceCounter(newstring4,unique_words)


# In[31]:


documents = {}

documents['file1'] = fileOccurence1
documents['file2'] = fileOccurence2
documents['file3'] = fileOccurence3
documents['file4'] = fileOccurence4


# In[125]:


#N (number of documents)
N=4
# IDF = [math.log(N/x) for x in text_occurrence_unique_words_corpus]

# function for sum of dict
def sum_dictionaries(dict1, dict2, dict3 ,dict4):
    result = {}

    for key in dict1:
        if key in dict2 and key in dict3 and key in dict4:
            result[key] = int(dict1[key]) + int(dict2[key]) + int(dict3[key])+ int(dict4[key])

    return result


# In[126]:


import math
# IDF = [math.log(N/x) for x in text_occurrence]

text_occurrence = sum_dictionaries(fileOccurence1,fileOccurence2,fileOccurence3,fileOccurence4)

IDF = {}
for key,x in text_occurrence.items():
    IDF[key]=[math.log(N/(x+1))]


# In[127]:


#make a list containing number of occurences of terms in texts

def count_unique_words(unique_words,newstring1):
    count_unique_words = []

    for i in range(len(unique_words)):
        count_unique_words.append(newstring1.count(unique_words[i]))
    return count_unique_words

# TF_text1 = [x/len(newstring1) for x in count_unique_words_text1]

def tf(newstring1,count_unique_words_text1):
    return [x/len(newstring1) for x in count_unique_words_text1]
     


# In[128]:


count_unique_words_text1 = count_unique_words(unique_words,newstring1)
count_unique_words_text2 = count_unique_words(unique_words,newstring2)
count_unique_words_text3 = count_unique_words(unique_words,newstring3)
count_unique_words_text4 = count_unique_words(unique_words,newstring4)

TF_text1 = tf(newstring1,count_unique_words_text1)
TF_text2 = tf(newstring2,count_unique_words_text2)
TF_text3 = tf(newstring3,count_unique_words_text3)
TF_text4 = tf(newstring4,count_unique_words_text4)


# In[129]:


## TF - IDF ##
def tfIDF(IDF,TF_text1):    
    TFIDF_text1 = []
    listIDF = list(IDF.items())

    for x in range(len(IDF)):
         TFIDF_text1.append(TF_text1[x]*listIDF[x][1][0])
    return TFIDF_text1


# In[130]:


TFIDF_text1 = tfIDF(IDF,TF_text1)
TFIDF_text2 = tfIDF(IDF,TF_text2)
TFIDF_text3 = tfIDF(IDF,TF_text3)
TFIDF_text4 = tfIDF(IDF,TF_text4)


# In[131]:


def displayTFIDF(unique_words,TFIDF_text1):
    TFIDF_text1.sort(reverse=True)  # Using sort() method
    tflist = []
    for i, x in enumerate(TFIDF_text1):
        nlist=[unique_words[i],x]
        tflist.append(nlist)
    return tflist


# In[132]:


file1 = displayTFIDF(unique_words,TFIDF_text1)
file2 = displayTFIDF(unique_words,TFIDF_text2)
file3 = displayTFIDF(unique_words,TFIDF_text3)
file4 = displayTFIDF(unique_words,TFIDF_text4)


# In[ ]:





# In[133]:


def render_html_table(data):
    
#     html = "<style>table{  margin:auto;   border-collapse: collapse; } th,td{border:1px solid black;padding:2%;}</style><table><tr><th>Key words</th> <th>Values</th></tr>"
    html = "<style>table {border-collapse: collapse;width: 100%;}th, td {padding: 8px;text-align: center;border-bottom: 1px solid #ddd;}th {background-color: #f2f2f2;font-weight: bold;}tr:nth-child(even) {background-color: #f9f9f9;}</style><table><tr><th>Key words</th> <th>Values</th></tr>"
    
    # Render table rows
    for row in data[1:]:
        html += "<tr>"
        for cell in row:
            html += f"<td>{cell}</td>"
        html += "</tr>"
    
    html += "</table>"
    return html



# In[134]:


def save_html_table_to_file(html_table, filename):
    with open(filename, "w") as file:
        file.write(html_table)

html_table = render_html_table(file1)
save_html_table_to_file(html_table, "file1.html")

html_table = render_html_table(file2)
save_html_table_to_file(html_table, "file2.html")


html_table = render_html_table(file3)
save_html_table_to_file(html_table, "file3.html")


html_table = render_html_table(file4)
save_html_table_to_file(html_table, "file4.html")


# In[ ]:




