import spacy
nlp = spacy.load('en_core_web_md')
tokens = nlp('cat apple monkey banana ')  
#Cat -> cat,apple, moneky,banana
#Apple -> cat,apple,m onkey, banana
#banana -> cat,apple,monkey,banana
for token1 in tokens:
    for token2 in tokens:  
        print(token1.text, token2.text, token1.similarity(token2))  



sentence_to_compare = "Why is my cat on the car"  
sentences = ["where did my dog go",  "Hello, there is my car",  "I\'ve lost my car in my car",  "I\'d like my boat back",  "I will name my dog Diana"]  
model_sentence = nlp(sentence_to_compare)  
for sentence in sentences:  
    similarity = nlp(sentence).similarity(model_sentence)  
    print(sentence + " - ", similarity)
    
#Another interesting fact is that cat does not have any significant similarity  with 
# any of the fruits although monkey does. Because, cats doesnt eat any fruits. So, the model does not  explicitly seem to 
# recognise transitive relationships in its calculation. 
#Cat, Meat, Monkey. Monekey doesnt eat meat.
#en_core_web_sm is a small dataset so it would give less precision similiraties. To solve this
#we need to use a larger dataset like en_core_web_md
