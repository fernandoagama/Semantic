import spacy

#Load the spacy in the memory
def load_spacy():
    nlp = spacy.load("en_core_web_md")
    return nlp

#Read the movies.txt
def read_movies():
    #Create a empty dict to fill with names and description of each movie
    dict_movies  = {}
    try:
        #Open movies.txt
        with open('movies.txt', 'r') as movies:
            for line in movies:
                #Split each line in name and description
                name, description =  line.split(':')
                #Store the name and description in the dict_movies
                #Where name is the key and description is the value
                dict_movies[name] = description
        #Return the filled dict
        return dict_movies
    except:
        print("File not found.")
        return -1

def get_movie_recommendations(description):
    #Load dict_movies with all movies
    dict_movies = read_movies()
    #Load spacy in nlp
    nlp = load_spacy()
    #Create an empty list to be filled with name of the movie and the similarity of the movie
    similarities = []
    #Tokenize description parameter
    token_desc_parameter = nlp(description)
    #Get in the dict_movies each name and description of each movie
    for name_movie,description_movie in dict_movies.items():
        #Tokenize description_movie and calculate the similarity of each description
        similarity = nlp(description_movie).similarity(token_desc_parameter)
        #Add in the list similarities the name of the movie and his similiarity
        similarities.append((name_movie,similarity))
    #Sort the list similiarities based by similarity and order by DESC
    #So we can get the first position, because his is the most similar movie
    similarities.sort(key=lambda similarity: similarity[1], reverse=True)
    index_name_movie = 0
    first_position = 0
    recommendation = similarities[first_position][index_name_movie]
    print("Watch next: ", recommendation)
            
get_movie_recommendations("Will he save  their world or destroy it? When the Hulk becomes too dangerous for the  Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a  planet where the Hulk can live in peace. Unfortunately, Hulk land on the  planet Sakaar where he is sold into slavery and trained as a gladiator.")