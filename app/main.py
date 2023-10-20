from flask import Flask, request, jsonify
import requests
import json
import psycopg2

app = Flask(__name__)

def write_questions(questions):
    '''Write question-answer-id into PostgreSQL database'''
    if questions:
        con = psycopg2.connect("dbname=questions user=root host=root")
        cur = con.cursor()
        insert_sql = """INSERT INTO questions_quiz VALUES(%s, %s, %s, %s)""" 
        for q in questions:
            cur.execute(insert_sql, [q['id'], q['question'], q['answer'], q['created_at']])
        con.commit()
        
@app.route('/post_endpoint', methods=['POST'])
def post_endpoint():
    '''Get number of questions from jservice.io and write questions to db with write_questions method'''
    if request.method == 'POST':
        data = request.get_json()
        if 'questions_num' in data:
            num = data['questions_num']
            try:
                # Отправляем запрос к публичному API для получения вопросов
                response = requests.get(f"https://jservice.io/api/random?count={num}")
                response.raise_for_status()
                questions = response.json()
                return questions
            except:
                raise Exception("Failed to fetch questions from the external API")       
        else:
            return jsonify({'error': 'Key "questions_num" not found'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=8000)