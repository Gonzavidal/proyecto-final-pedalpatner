from flask import Blueprint, jsonify, request, render_template

bpMain = Blueprint('bpMain', __name__)

@bpMain.route('/')
def main():
    return jsonify({"msg":"Bienvenidos a PedalPatner desde Main"})