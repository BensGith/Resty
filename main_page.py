from flask import Blueprint, render_template, request, session, flash, redirect

mainBP = Blueprint("main_page", __name__, static_folder="static", template_folder="templates")


@mainBP.route("/", methods=["GET"])
def main_page():
    if request.method == "GET":
        return render_template("main_page.html")