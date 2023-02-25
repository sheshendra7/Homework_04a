import requests
import json
import datetime



def my_brand(homework_name):
    print("==== Sheshendra Desiboyina ====")
    print("==== Course 2023S-SSW567-A ==== ")
    print("==== The name of the homework assignment: {} ==== ".format(homework_name))
    print("==== Date and time: {} ==== ".format(datetime.datetime.now()))

def Tester_mind(user_id):
    url = f"https://api.github.com/users/{user_id}/repos"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve data!")
        return "Failed to retrieve data!"
        sys.exit()
    repos = json.loads(response.text)

    if len(repos) <= 0:
        print("No repositories created")
        return "No repositories created"
        sys.exit()
    results = []
    for repo in repos:
        name = repo["name"]
        url = f"https://api.github.com/repos/{user_id}/{name}/commits"
        response = requests.get(url)
        commits = json.loads(response.text)
        count = len(commits)
        print(f"Repo: {name} Number of commits: {count}")
        results.append((name, count))

   # print(results)
    return results



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
 #   print_hi('PyCharm')
    my_brand("Homework 04a - Develop with the Perspective of the Tester in mind")
    Repo_Name = input("Enter the Repository Name")
    Tester_mind(Repo_Name)


