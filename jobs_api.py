from flask import jsonify, Blueprint, request

from data import db_session
from data.jobs import Jobs

blueprint = Blueprint('jobs_api', __name__, template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():
    @blueprint.route('/api/news/<int:news_id>', methods=['GET'])
    def get_one_news(news_id):
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).get(news_id)
        if not jobs:
            return jsonify({'error': 'Not found'})
        return jsonify(
            {
                'jobs': jobs.to_dict(only=(
                    'team_leader', 'job', 'work_size', 'collaborations', 'is_finished'))
            }
        )


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_one_job(job_id):
    session = db_session.create_session()

    # Получите список работ с идентификатором job_id

    return jsonify(...)  # Верните список работ с идентификтором job_id


@blueprint.route('/api/jobs', methods=['POST'])
def create_job():

    # Проверьте, что запрос содержит данные в формате json,
    # а также, что данный json содержит все требуемые поля данных
    # При необходимости верните сообщение об ошибке в нужном формате

    session = db_session.create_session()

    # Если работа с таким идентификатором уже существует в базе данных,
    # верните сообщение об ошибке в нужном формате

    job = Jobs(
        id=request.json['id'],
        ...  # Проинициализируйте оставшиеся поля
    )

    # Сохраните объект job в базе данных

    return jsonify(...)  # Верните сообщение об успехе
