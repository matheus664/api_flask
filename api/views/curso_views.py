from flask_restful import Resource
from flask import  render_template
from api import api
from ..schemas import curso_schema
from flask import request, make_response , jsonify
from ..entidades import curso
from ..services import curso_service
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import engine


class Cursolist (Resource):
    def get(self):
        cursos = curso_service.listar_cursos()
        return jsonify(cursos)


    def post (self):
        cs = curso_schema.CursoSchema()
        validate = cs.validate(request.json, session=1)
        if validate :
            return make_response(jsonify(validate), 400)
        else :
            nome = request.json["nome"]
            descricao = request.json ["descricao"]
            data_publicacao = request.json ["data_publicacao"]

            novo_curso = curso.Curso(nome=nome,descricao=descricao, data_publicacao=data_publicacao )
            resultado = curso_service.cadastrar_curso(novo_curso)
            return jsonify(nome, descricao, data_publicacao)












api.add_resource(Cursolist, "/cursos")








