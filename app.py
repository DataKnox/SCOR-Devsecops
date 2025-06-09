import os

def get_secret():
    password = "hardcoded_password"  # Bandit will flag this
    return password

def dangerous_eval(user_input):
    return eval(user_input)  # Bandit will flag this as HIGH
