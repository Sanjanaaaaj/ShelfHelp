from flask import Flask,request,render_template
import pickle
import pandas as pd
app=Flask(__name__)

books=pickle.load(open('books.pkl','rb'))
print(books.columns)
@app.route('/',methods=['GET'])
def index():
    #print(books["NAMES"])
    return render_template('index.html',
                           book=books
                           )

def recommend_top_books_by_genre(genre):
    genre_books = books[books['GENRE'].str.contains(genre, case=False, na=False)]
    top_books = genre_books.sort_values(by='RATING', ascending=False).head(10)
    return top_books[['BOOK-IDS', 'NAMES', 'GENRE', 'RATING','BOOK-URLS','IMAGE URLS']]

@app.route('/recommend', methods=['GET'])
def recommend():
    genre = request.args.get('genre')
    if genre:
        recommended_books = recommend_top_books_by_genre(genre)
        #print(recommended_books[['IMAGE URLS', 'NAMES']])  # Debugging to check the data
        return render_template('recommend.html', books=recommended_books.to_dict(orient='records'))
    return render_template('recommend.html', books=[])


if __name__=="__main__":
    app.run(debug=True)