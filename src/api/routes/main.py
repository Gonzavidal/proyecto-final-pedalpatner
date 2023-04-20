from flask import Blueprint, jsonify, request, render_template

bpMain = Blueprint('bpMain', __name__)

@bpMain.route('/')
def main():
    return jsonify({"msg":"Bienbenidos a PedalPatner desde Main"})