from flask_restplus import Api, Resource, reqparse
from flask import Flask, jsonify, request   
from config.databases import mycollection
from config.app import config
from bson import ObjectId
from helpers import helpers
import json

app = Flask(__name__)
api = Api(app, version='1.0', title='Sitrack', description='Sitrack test')

@api.route('/alphabetSoup')
class AlphabetSoupList(Resource):

    # Check payload (Documentation)
    parser = reqparse.RequestParser()
    parser.add_argument("w", type=int, help='Number of soup columns', required=True, location='form')
    parser.add_argument('h', type=int, help='Number of soup rows', required=True, location='form')
    parser.add_argument('ltr', type=bool, help='Add words from left to right', location='form')
    parser.add_argument('ttb', type=bool, help='Add words form top to botton', location='form')

    """
    Creates a new alphabet soup
    """

    @api.expect(parser)
    def post(self):

        input_data = request.get_json()
        col = input_data["w"]
        row = input_data["h"]
        ltr = input_data["ltr"]
        ttb = input_data["ttb"]
        wordstofind = []
        alphabetsoup = {
            "soup" : [],
            "words" : []
        }
    
        soup_data = {}

        # Check input data
        if row<=80 and row>=15 and col<=80 and col>=15:
            matrix = helpers.word_soup_create(col, row) 
        else:
            return api.abort(400,"Error, the word soup can not be smaller than 15 nor larger than 80 chars")
        
        if ltr == "":
            ltr = "true"
        if ttb == "":
            ttb = "true"

        # Once the default matrix is created, it is then randomized
        matrix = helpers.word_soup_randomize(matrix,col, row)

        # If parameter "ltr" is true, a random word is inserted from left to right
        if ltr == "true": 
            soup_data = helpers.word_soup_addltr(matrix, col, row)
            wordstofind.extend(soup_data["word"])

        # if parameter "ttb" is true, a random word is inserted from top to bottom
        if ttb == "true": 
            soup_data = helpers.word_soup_addttb(soup_data["matrix"], col, row)
            wordstofind.extend(soup_data["word"])

        # The word soup is finally saved into the DB
        alphabetsoup["soup"] = soup_data["matrix"]
        alphabetsoup["words"] = wordstofind
        soup = mycollection.insert_one(alphabetsoup)

        # The id of the object is returned
        return jsonify(id=str(soup.inserted_id))

@api.doc(params={'id': 'The alphabetSoup id'})
@api.route('/alphabetSoup/view/<string:id>')
class AlphabetSoup(Resource):

    """
    Displays an alphabet soup
    """

    def get(self,id):

        word_soup_string = ""
        oid = ObjectId(id)

        # TODO: add validation of object id, if fail then send error message

        query = list(mycollection.find({"_id": oid},{"words":0,"_id":0}))
        data = {"soup": query[0]["soup"]}

        for lists in data["soup"]:
            word_soup_string = word_soup_string + "|".join(lists) + "\n"
        output = word_soup_string.split("\n")

        return jsonify(soup=output)
        
@api.doc(params={'id': 'The alphabetSoup id'})
@api.route('/alphabetSoup/list/<string:id>')
class WordList(Resource):

    """
    Displays the words that can be found for a given id
    """

    def get(self,id):

        oid = ObjectId(id)

        # TODO: add validation of object id, if fail then send error message

        query = list(mycollection.find({"_id": oid},{"soup":0,"_id":0}))
        data = {"words": query[0]["words"]}

        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=config["debug"], port=config["port"])
  