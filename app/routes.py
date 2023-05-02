from flask import Blueprint, jsonify, request
from app.models.lesson import Lesson
from app import db

# CRUD


# Read
# SET UP AN ENDPOINT:
#  Expected request:
#    /lessons GET (to get all lessons data)
#  Expected response:
#    JSON list with JSON dictionaries (objects) of lesson data
#    status code of 200 OK

lessons_bp = Blueprint('thisisthelessonsblueprint', __name__, url_prefix='/lessons')

@lessons_bp.route('', methods=['GET'])
def get_all_lessons():
    # get all lesson data
    all_lessons = Lesson.query.all()

    # format it into my own ideal json response
    lesson_response = []
    for lesson in all_lessons:
        lesson_response.append({
            "simonhasareasontomakethisaspecificname": lesson.id,
            "lessonTitle": lesson.title,
            "lesson_description": lesson.description
        })

    return jsonify(lesson_response), 200

# CREATE
# SET UP AN ENDPOINT:
#  Expected request:
#    /lessons POST
#  Expected response:
#    String that says "lesson of id {} is created" 201 Created

@lessons_bp.route('', methods=['POST'])
def create_lesson():
    # Read new lesson data from request body
    request_body = request.get_json()

    # Make new lesson
    new_lesson = Lesson(
        title=request_body["title"],
        description=request_body["description"]
    )

    # Save to database
    db.session.add(new_lesson)
    db.session.commit()

    return f"Lesson of {new_lesson.id} is created", 201
