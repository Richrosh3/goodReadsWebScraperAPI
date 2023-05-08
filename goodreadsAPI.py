from flask import Flask, jsonify
from webScraper import scrape_reviews

app = Flask(__name__)

@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    reviews = scrape_reviews()

    print(reviews)

    return jsonify(reviews)

if __name__ == "__main__":
    app.run(debug=True)