from flask import blueprints
from requests import get
 
users_github = blueprints("users_github", __name__)

@users_github.route("/github/users", methods=['POST'])
def github():
    data = request.get_json()
    country = data['country']
    return get(f'https://api.github.com/search/users?q=location:"{country}"&page=1').json()


