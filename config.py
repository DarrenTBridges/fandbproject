import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        "postgres://iqzepczsapjjoz:3cef1cf46aacdd8f5bc36c7e5f527c5f97157c8660001380b45cf91cf7547919@ec2-52-31-233-101.eu-west-1.compute.amazonaws.com:5432/d1hbdtja7o8kvo"
    SQLALCHEMY_TRACK_MODIFICATIONS = False