from flask import Blueprint, request, jsonify
from app.utils.nlp_model import predict_scam
from app import db
from Database.jobModel import JobModel


main_bp = Blueprint("main", __name__)


@main_bp.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to JobShield API"})


@main_bp.route("/show-data", methods=["GET"])
def show_data():
    jobs = JobModel.query.all()
    return jsonify([job.serialize() for job in jobs]), 200

    
@main_bp.route("/verify", methods=["GET"])
def verify():
    text = request.args.get("description", "")
    result = predict_scam(text)

    job=JobModel(
        description=text,
        scam=result["scam"],
        confidence=result["confidence"]
        )

    if not JobModel.query.filter_by(description=text).first():
        db.session.add(job)
        db.session.commit()

    print('record added to database')
    if not text:
        return jsonify({"error": "Missing 'description' field"}), 400

    return jsonify(result)

@main_bp.route("/get-by-id/<int:id>", methods=["GET"])
def get_by_id(id):
    job = JobModel.query.get(id)
    if job:
        return jsonify(job.serialize()), 200
    return jsonify({"error": "Job not found"}), 404


@main_bp.route("/delete/<int:id>", methods=["GET"])
def delete_job(id):
    job = JobModel.query.get(id)
    if job:
        db.session.delete(job)
        db.session.commit()
        return jsonify({"message": "Deleted successfully"}), 200
    return jsonify({"error": "Job not found"}), 404
