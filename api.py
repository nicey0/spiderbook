#-Imports--------------------------------------------------#
import os

from flask import Flask, request, redirect, make_response, render_template, url_for, jsonify
from flask_script import Manager

from API.db_management import create_post, get_posts

#-Functions------------------------------------------------#
